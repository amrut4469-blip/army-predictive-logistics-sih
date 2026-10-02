# 🤖 RASAD-AI — AI/ML Model Documentation

## 1. Overview

RASAD-AI uses predictive analytics and machine-learning techniques to estimate future logistics demand.

The AI/ML component is designed to answer a core planning question:

> **What quantity of a supported supply category may be required at a given location during a future planning period?**

The forecast is then used by the inventory and risk modules to support requirement prioritization and delivery planning.

The overall ML pipeline is:

```text
Historical Data
      ↓
Data Validation
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Train / Validation Split
      ↓
Model Training
      ↓
Forecast Generation
      ↓
Model Evaluation
      ↓
Demand Prediction
      ↓
Risk & Planning Modules
```

---

# 2. AI/ML Objectives

The AI/ML component has the following objectives:

### Objective 1 — Forecast Future Demand

Estimate future consumption for supported supply categories.

### Objective 2 — Identify Demand Trends

Detect patterns in historical consumption.

### Objective 3 — Support Inventory Planning

Use predicted demand to estimate future inventory coverage.

### Objective 4 — Support Risk Assessment

Use forecast demand as one input to stock-out risk analysis.

### Objective 5 — Improve Planning Efficiency

Provide machine-assisted estimates that can reduce repetitive manual calculations.

---

# 3. Input Data

The forecasting system can use historical observations such as:

| Feature          | Description                                 |
| ---------------- | ------------------------------------------- |
| Date             | Date of observation                         |
| Location ID      | Supported location identifier               |
| Supply Category  | Type of supply                              |
| Consumption      | Historical consumption                      |
| Inventory        | Available inventory                         |
| Personnel        | Authorized/synthetic planning information   |
| Weather          | Synthetic or authorized weather information |
| Previous Demand  | Historical demand values                    |
| Delivery History | Previous delivery information               |

The exact feature set depends on the final dataset and implemented model.

---

# 4. Data Pipeline

The first stage of the ML system is data preparation.

```text
Raw Dataset
     ↓
Schema Validation
     ↓
Missing Value Handling
     ↓
Duplicate Removal
     ↓
Outlier Analysis
     ↓
Normalization / Transformation
     ↓
Feature Engineering
     ↓
Model Dataset
```

---

# 5. Data Validation

Before model training, the dataset should be checked for:

* Missing values
* Invalid dates
* Duplicate records
* Invalid numerical values
* Incorrect categories
* Unexpected data ranges
* Inconsistent units

Example:

```text
Input Record
     ↓
Is Date Valid?
     ↓
Is Demand Valid?
     ↓
Are Required Fields Present?
     ↓
Valid Record
```

Invalid records should be flagged or handled according to the preprocessing strategy.

---

# 6. Feature Engineering

Feature engineering converts raw observations into useful model inputs.

Potential features include:

### Temporal Features

* Day
* Week
* Month
* Quarter
* Day of week

### Historical Demand Features

* Previous-day demand
* Previous-week demand
* Rolling average
* Rolling standard deviation
* Historical trend

### Context Features

Depending on available authorized data:

* Inventory
* Personnel count
* Weather indicators
* Delivery history
* Other relevant variables

Feature selection should be based on data availability and validation results.

---

# 7. Time-Series Considerations

Because logistics consumption is observed over time, the forecasting pipeline should preserve chronological ordering.

A conventional random train/test split can introduce future information into the training dataset.

Instead, a time-aware approach should be used.

Example:

```text
Historical Data
──────────────────────────────────────────────► Time

|──────── Training ────────|── Validation ──|── Test ──|
```

This helps evaluate how the model performs when predicting future observations from past information.

---

# 8. Candidate Models

The project can evaluate multiple forecasting approaches.

Potential models include:

## 8.1 Baseline Model

A simple baseline should be established first.

Examples:

* Moving average
* Previous-period demand
* Seasonal baseline

The baseline provides a reference point for evaluating more complex models.

---

## 8.2 Statistical Time-Series Models

Traditional time-series models can be useful when historical patterns are relatively stable.

Possible approaches include:

* Exponential smoothing
* ARIMA-family models
* Seasonal models

---

## 8.3 Prophet

Prophet can be considered for time-series forecasting with trend and seasonal components.

Conceptual workflow:

```text
Historical Date + Demand
          ↓
       Prophet
          ↓
   Future Forecast
```

---

## 8.4 XGBoost

XGBoost can be used as a supervised regression approach.

Potential features:

```text
Lag Demand
Rolling Mean
Rolling Std
Month
Week
Inventory
Other Features
```

Output:

```text
Predicted Demand
```

---

## 8.5 LSTM

An LSTM neural network can be considered for sequential demand patterns when sufficient training data is available.

Conceptual flow:

```text
Historical Sequence
        ↓
     LSTM Model
        ↓
Future Demand
```

LSTM should only be selected when the available dataset justifies the additional complexity.

---

# 9. Model Selection

The system should not assume that the most complex model is automatically the best model.

Models should be compared using:

* Validation performance
* Stability
* Computational cost
* Data requirements
* Interpretability
* Deployment constraints

A model can be selected based on measured validation results.

---

# 10. Training Pipeline

The conceptual training pipeline is:

```text
Dataset
   ↓
Preprocessing
   ↓
Feature Engineering
   ↓
Time-Based Split
   ↓
Baseline
   ↓
Candidate Models
   ↓
Training
   ↓
Validation
   ↓
Model Comparison
   ↓
Selected Model
```

---

# 11. Forecast Generation

Once a model has been trained and validated, it can generate future demand estimates.

```text
Latest Historical Data
        ↓
Selected Model
        ↓
Forecast Horizon
        ↓
Predicted Demand
```

Example:

```text
Day 1 → 48 units
Day 2 → 51 units
Day 3 → 53 units
Day 4 → 49 units
Day 5 → 55 units
```

These values are illustrative only.

---

# 12. Forecast Horizon

The forecast horizon depends on the planning requirements.

Possible horizons include:

* Short-term
* Weekly
* Multi-week

The final horizon should be configurable according to the prototype requirements.

---

# 13. Model Evaluation

Forecast quality should be measured using appropriate metrics.

## MAE — Mean Absolute Error

Measures average absolute prediction error.

```text
MAE = average(|Actual - Predicted|)
```

Lower values indicate smaller average absolute errors.

---

## RMSE — Root Mean Squared Error

RMSE gives greater weight to larger errors.

```text
RMSE = √(average((Actual - Predicted)²))
```

Lower values indicate smaller prediction errors.

---

## MAPE

MAPE can measure percentage-based error when the underlying data is suitable for percentage calculations.

Care should be taken when actual demand values are zero or very close to zero.

---

# 14. Baseline Comparison

The ML model should be compared with a simple baseline.

Example:

```text
                 Forecast Error
Baseline        →  X
ML Model        →  Y
```

The system should report the actual measured values.

The project should not claim improvement unless it has been demonstrated through validation.

---

# 15. Cross-Validation

For time-series data, validation should preserve temporal order.

Possible approaches include:

* Rolling-window validation
* Expanding-window validation
* Time-based holdout

Conceptual example:

```text
Fold 1:
Train →→→ Validation

Fold 2:
Train →→→→ Validation

Fold 3:
Train →→→→→ Validation
```

This provides a more realistic estimate of future forecasting performance.

---

# 16. Overfitting Prevention

The model should be evaluated for overfitting.

Potential techniques include:

* Time-aware validation
* Regularization
* Feature selection
* Early stopping where applicable
* Model complexity control
* Monitoring training vs validation performance

The objective is to produce a model that generalizes to unseen observations.

---

# 17. Uncertainty and Forecast Interpretation

Forecasts are estimates rather than guaranteed future values.

Where supported, the system can provide:

* Prediction intervals
* Confidence information
* Historical error metrics
* Model version
* Forecast timestamp

Example:

```text
Predicted Demand: 500 units
Estimated Range: 450–560 units
```

The exact uncertainty method depends on the selected model.

---

# 18. Forecast → Inventory Integration

The forecast becomes an input to the inventory analysis module.

Conceptual flow:

```text
Predicted Demand
       +
Current Inventory
       ↓
Inventory Coverage
       ↓
Risk Assessment
```

A simplified coverage calculation is:

```text
Coverage Days =
Current Inventory / Estimated Daily Demand
```

This is a prototype calculation and should be adapted to the actual inventory and demand model.

---

# 19. Forecast → Risk Integration

The risk engine can combine:

* Current inventory
* Forecast demand
* Expected consumption
* Planning horizon

to estimate potential stock-out risk.

```text
Forecast
   ↓
Expected Consumption
   ↓
Inventory Projection
   ↓
Potential Stock-Out
   ↓
Risk Indicator
```

---

# 20. Forecast → Optimization Integration

Forecasting and optimization are separate modules but can work together.

```text
                ┌─────────────────┐
Historical Data │                 │
───────────────►│ Forecast Model  │
                │                 │
                └───────┬─────────┘
                        ↓
                 Forecast Demand
                        ↓
                ┌─────────────────┐
                │ Risk / Priority │
                └───────┬─────────┘
                        ↓
                ┌─────────────────┐
                │ Optimization    │
                └───────┬─────────┘
                        ↓
                 Candidate Plan
```

This separation makes it possible to improve the forecasting model without redesigning the optimization engine.

---

# 21. Explainability

The system should provide understandable information about the forecast.

Possible explanations include:

* Historical demand trend
* Recent demand changes
* Important input features
* Forecast horizon
* Model used
* Model evaluation metrics

For complex models, additional explainability techniques can be considered.

The purpose is to help authorized users understand the analytical output rather than treating the prediction as unquestionable.

---

# 22. Model Versioning

Each production-like model should have identifiable metadata.

Example:

```text
Model Name: Demand Forecast Model
Model Version: 1.0
Training Date: YYYY-MM-DD
Training Dataset Version: DATASET_VERSION
Forecast Horizon: CONFIGURED_HORIZON
Evaluation Metrics: MAE / RMSE
```

The actual values should be generated from the implemented pipeline.

---

# 23. Model Monitoring

After deployment or demonstration, model performance should be monitored.

Potential indicators include:

* Forecast error
* Data drift
* Prediction stability
* Missing data rate
* Inference latency

Conceptual workflow:

```text
New Data
   ↓
Prediction
   ↓
Actual Observation
   ↓
Error Calculation
   ↓
Performance Monitoring
   ↓
Model Review
```

---

# 24. Retraining Strategy

The model may be retrained when:

* Sufficient new data becomes available
* Forecast error increases
* Data distribution changes
* A new model performs better
* Feature availability changes

Retraining should be controlled and evaluated before replacing an existing model.

---

# 25. ML Pipeline Architecture

```text
┌──────────────────────────┐
│ Synthetic / Authorized   │
│ Historical Dataset       │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Data Validation          │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Preprocessing            │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Feature Engineering      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Baseline Models          │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Candidate ML Models      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Time-Based Validation    │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Model Selection          │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Forecast Generation      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Risk / Planning Modules  │
└──────────────────────────┘
```

---

# 26. Example Synthetic Dataset

A simplified dataset may look like:

| Date       | Location | Category | Consumption | Inventory |
| ---------- | -------- | -------- | ----------: | --------: |
| 2026-01-01 | LOC-001  | Ration   |          48 |       600 |
| 2026-01-02 | LOC-001  | Ration   |          51 |       552 |
| 2026-01-03 | LOC-001  | Ration   |          49 |       501 |
| 2026-01-04 | LOC-001  | Ration   |          53 |       452 |
| 2026-01-05 | LOC-001  | Ration   |          50 |       399 |

These values are fictional and intended only to demonstrate the data format.

---

# 27. Example Prediction

Suppose the model receives recent synthetic observations:

```text
48
51
49
53
50
```

The model may produce:

```text
Next-Day Forecast = 52 units
```

This prediction is then passed to the inventory analysis module.

Again, this is an illustrative example rather than a measured model output.

---

# 28. Model Testing

The ML implementation should include tests for:

### Data Processing

* Missing-value handling
* Date parsing
* Feature generation

### Model

* Training completes successfully
* Prediction output is valid
* Expected output shape

### Evaluation

* Metrics are calculated correctly
* Zero-demand cases are handled appropriately

### Integration

* Forecast output can be consumed by the risk engine
* Forecast output can be passed to downstream planning modules

---

# 29. AI/ML Responsible Use

The AI component is designed as decision support.

Important principles:

* Predictions are estimates.
* Models require validation.
* Data quality affects model quality.
* Model outputs should be reviewed by authorized users.
* No sensitive operational information should be placed in the public repository.
* The system should not independently execute operational decisions.

---

# 30. Current Prototype Status

The AI/ML documentation describes the proposed and configurable analytical pipeline.

The repository should clearly distinguish between:

### Implemented

Components that are actually present and tested in the source code.

### Prototype

Components implemented for demonstration.

### Planned

Components described in the architecture but not yet implemented.

This distinction prevents documentation from overstating the capabilities of the current prototype.

---

# 31. Summary

The RASAD-AI AI/ML pipeline follows a structured process:

```text
Data
 ↓
Validation
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Baseline
 ↓
Candidate Models
 ↓
Validation
 ↓
Model Selection
 ↓
Forecast
 ↓
Inventory Analysis
 ↓
Risk Assessment
 ↓
Optimization
```

The approach emphasizes measurable model evaluation, time-aware validation, explainability, and human review.

The use of synthetic data allows the project to demonstrate the technical concept without exposing sensitive operational information.
