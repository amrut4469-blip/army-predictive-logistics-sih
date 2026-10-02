"""
Synthetic data generator for forward-post logistics.

NOTE: All data is SYNTHETIC. No real military data is used.
Consumption = troops x per-capita rate x altitude x season x heating x surge x noise.
"""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
OUT = Path(__file__).parent / "sample"

# name, altitude_m, troops, distance_from_depot_km
POSTS = [
    ("Post Alpha",   3200, 120,  85),
    ("Post Bravo",   3800, 80,  140),
    ("Post Charlie", 4300, 60,  190),
    ("Post Delta",   4800, 45,  240),
    ("Post Echo",    5200, 30,  290),
    ("Post Foxtrot", 3500, 150, 110),
    ("Post Golf",    4100, 70,  170),
    ("Post Hotel",   5500, 25,  320),
]
# per-soldier daily need in kg
CATEGORIES = {"ration": 1.8, "fuel": 1.2, "medical": 0.15, "ammo": 0.4}


def season_factor(doy):
    """Winter (Dec-Feb) raises fuel/ration demand; peaks around day 20."""
    return 1 + 0.35 * np.cos(2 * np.pi * (doy - 20) / 365)


def generate(days=730, seed=SEED):
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2024-01-01", periods=days, freq="D")
    doy = dates.dayofyear.values
    sf = season_factor(doy)

    posts = pd.DataFrame(POSTS, columns=["post", "altitude_m", "troops", "distance_km"])
    posts["post_id"] = range(len(posts))

    rows = []
    for _, p in posts.iterrows():
        # weather: colder with altitude, snow mostly in winter
        temp = 18 - 0.0065 * p.altitude_m - 14 * (sf - 1) + rng.normal(0, 2.5, days)
        snow_cm = np.clip(
            rng.gamma(0.6, 4, days) * (sf - 0.9) * 3 * (p.altitude_m / 4000), 0, None
        )
        # road closure more likely with heavy snow and higher altitude
        p_close = np.clip(snow_cm / 60 + (p.altitude_m - 3000) / 20000, 0, 0.9)
        road_closed = rng.random(days) < p_close

        alt_factor = 1 + (p.altitude_m - 3000) / 10000

        # operational surges: ~10-day windows, known in advance
        op_tempo = np.zeros(days)
        for start in rng.choice(days - 12, size=days // 60, replace=False):
            op_tempo[start:start + 10] = 1

        for cat, rate in CATEGORIES.items():
            cat_season = sf if cat in ("fuel", "ration") else 1.0
            heating = 1 + 0.03 * np.clip(0 - temp, 0, None) if cat == "fuel" else 1.0
            surge = 1 + 0.45 * op_tempo if cat in ("ration", "ammo", "fuel") else 1.0
            base = p.troops * rate * alt_factor * cat_season * heating * surge
            consumption = np.clip(base * rng.normal(1, 0.07, days), 0, None)
            rows.append(pd.DataFrame({
                "date": dates,
                "post_id": p.post_id,
                "category": cat,
                "consumption_kg": consumption.round(2),
                "temp_c": temp.round(1),
                "snow_cm": snow_cm.round(1),
                "op_tempo": op_tempo,
                "road_closed": road_closed,
            }))

    return {"posts": posts, "consumption": pd.concat(rows, ignore_index=True)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, df in generate().items():
        df.to_csv(OUT / f"{name}.csv", index=False)
        print(f"wrote {OUT / (name + '.csv')}  ({len(df):,} rows)")


if __name__ == "__main__":
    main()
