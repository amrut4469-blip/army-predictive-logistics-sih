"""
Demand forecasting: baseline (7-day moving average) vs Gradient Boosting.
Reports MAPE on a time-based hold-out (last 60 days).
Only lagged / known-in-advance features are used, so there is no data leakage.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

sys.path.append(str(Path(__file__).resolve().parents[2]))
from data.generate import generate  # noqa: E402

HOLDOUT_DAYS = 60


def mape(y, yhat):
    y, yhat = np.asarray(y), np.asarray(yhat)
    return float(np.mean(np.abs((y - yhat) / np.clip(y, 1e-6, None))) * 100)


def build_features(df, posts):
    df = df.sort_values(["post_id", "category", "date"]).copy()
    g = df.groupby(["post_id", "category"])["consumption_kg"]
    df["lag1"] = g.shift(1)
    df["lag7"] = g.shift(7)
    df["ma7"] = g.transform(lambda x: x.shift(1).rolling(7).mean())
    df["doy"] = df["date"].dt.dayofyear
    df["dow"] = df["date"].dt.dayofweek
    df["cat_code"] = df["category"].astype("category").cat.codes
    df = df.merge(posts[["post_id", "altitude_m", "troops"]], on="post_id")
    return df.dropna()


def run(days=730):
    data = generate(days)
    df = build_features(data["consumption"], data["posts"])

    cutoff = df["date"].max() - pd.Timedelta(days=HOLDOUT_DAYS)
    train = df[df["date"] <= cutoff]
    test = df[df["date"] > cutoff]

    # weather forecast + planned operations are known ahead of time
    feats = ["lag1", "lag7", "ma7", "doy", "dow", "cat_code",
             "altitude_m", "troops", "temp_c", "snow_cm", "op_tempo"]

    model = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.08, random_state=0)
    model.fit(train[feats], train["consumption_kg"])

    res = {
        "baseline_ma7_mape": mape(test["consumption_kg"], test["ma7"]),
        "gbm_mape": mape(test["consumption_kg"], model.predict(test[feats])),
    }
    res["improvement_pct"] = 100 * (1 - res["gbm_mape"] / res["baseline_ma7_mape"])
    return res


if __name__ == "__main__":
    r = run()
    print(f"Baseline (7-day MA) MAPE : {r['baseline_ma7_mape']:.2f}%")
    print(f"Gradient Boosting  MAPE  : {r['gbm_mape']:.2f}%")
    print(f"Improvement              : {r['improvement_pct']:.1f}%")
