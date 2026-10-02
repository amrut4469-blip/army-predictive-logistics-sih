# 🔄 RASAD-AI — System Workflow

## 1. Overview

RASAD-AI follows an end-to-end decision-support workflow that connects data processing, demand forecasting, inventory analysis, risk assessment, requirement prioritization, route optimization, and dashboard visualization.

The objective is to transform historical and current logistics information into structured planning insights for authorized users.

The overall workflow is:

```text
Data
 ↓
Validation
 ↓
Processing
 ↓
Forecasting
 ↓
Inventory Analysis
 ↓
Risk Assessment
 ↓
Prioritization
 ↓
Route Optimization
 ↓
Dashboard
 ↓
Human Review
 ↓
Planning Output
 ↓
Feedback
```

---

# 2. End-to-End Workflow

```text
┌────────────────────────────┐
│ 1. DATA COLLECTION         │
│                            │
│ Consumption                │
│ Inventory                  │
│ Personnel                  │
│ Vehicles                   │
│ Weather                    │
│ Route Status               │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 2. DATA VALIDATION         │
│                            │
│ Missing Values             │
│ Invalid Records            │
│ Duplicate Records          │
│ Schema Validation          │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 3. DATA PROCESSING         │
│                            │
│ Cleaning                   │
│ Transformation             │
│ Aggregation                │
│ Feature Engineering        │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 4. DEMAND FORECASTING      │
│                            │
│ Historical Trends          │
│ ML / Statistical Model     │
│ Future Demand              │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 5. INVENTORY ANALYSIS      │
│                            │
│ Current Stock              │
│ Forecast Demand            │
│ Estimated Coverage         │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 6. RISK ASSESSMENT         │
│                            │
│ Stock-Out Risk             │
│ Coverage Level             │
│ Requirement Severity       │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 7. PRIORITIZATION          │
│                            │
│ Requirements               │
│ Risk                       │
│ Constraints                │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 8. ROUTE OPTIMIZATION      │
│                            │
│ Vehicles                   │
│ Capacity                   │
│ Route Constraints          │
│ Delivery Requirements      │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 9. COMMAND DASHBOARD       │
│                            │
│ Forecasts                  │
│ Risks                      │
│ Inventory                  │
│ Routes                     │
│ Scenarios                  │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 10. HUMAN REVIEW           │
│                            │
│ Authorized User Review     │
│ Validation                 │
│ Approval / Modification    │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 11. PLANNING OUTPUT        │
│                            │
│ Reviewed Delivery Plan     │
│ Priority Requirements      │
│ Planning Information       │
└──────────────┬─────────────┘
               ↓
┌────────────────────────────┐
│ 12. FEEDBACK               │
│                            │
│ Actual Consumption         │
│ Actual Results             │
│ Model Evaluation           │
└──────────────┬─────────────┘
               │
               └──────────→ Future Forecasting
```

---

# 3. Step 1 — Data Collection

The system begins with historical and current data.

Potential input categories include:

| Category    | Example                                  |
| ----------- | ---------------------------------------- |
| Consumption | Historical usage                         |
| Inventory   | Current stock                            |
| Supply      | Supply category                          |
| Location    | Supported location identifier            |
| Personnel   | Authorized planning information          |
| Vehicle     | Vehicle capacity and availability        |
| Weather     | Authorized/synthetic weather information |
| Route       | Route availability/status                |
| Delivery    | Planned/completed delivery records       |

For the prototype, synthetic data is used.

---

# 4. Step 2 — Data Validation

Before data is used by analytical components, it should pass validation checks.

Validation can include:

### Required Fields

Ensure required fields are present.

### Data Types

Verify that values have the expected type.

### Range Checks

Identify impossible or suspicious values.

### Duplicate Detection

Detect duplicate records.

### Missing Data

Identify missing observations and apply an appropriate handling strategy.

Example:

```text
Raw Record
    ↓
Schema Check
    ↓
Value Validation
    ↓
Duplicate Check
    ↓
Missing Data Check
    ↓
Validated Record
```

---

# 5. Step 3 — Data Processing

Validated data is transformed into a format suitable for analytics.

Processing may include:

* Date normalization
* Aggregation
* Feature creation
* Unit normalization
* Historical trend calculation
* Inventory calculations

Example:

```text
Daily Consumption
       ↓
Weekly Aggregation
       ↓
Historical Demand Series
       ↓
Forecasting Dataset
```

---

# 6. Step 4 — Demand Forecasting

The forecasting module estimates future requirements.

Conceptual workflow:

```text
Historical Data
      ↓
Feature Engineering
      ↓
Training Dataset
      ↓
Forecasting Model
      ↓
Validation
      ↓
Future Demand
```

Possible models include:

* Statistical time-series models
* Prophet
* XGBoost
* LSTM
* Other suitable models

The actual model should be selected based on measured validation performance and project requirements.

---

# 7. Step 5 — Inventory Analysis

The system compares current inventory with expected future demand.

A simplified calculation is:

```text
Current Inventory
       ÷
Estimated Daily Demand
       =
Approximate Days of Coverage
```

For example, if a simulated location has:

```text
Current Inventory = 500 units
Estimated Daily Demand = 50 units/day
```

then:

```text
Estimated Coverage = 500 / 50
                   = 10 days
```

This is an illustrative calculation for the prototype.

---

# 8. Step 6 — Stock-Out Risk Assessment

The risk engine uses inventory coverage and projected demand to identify potential supply shortages.

Prototype interpretation:

```text
Coverage > 7 days
        ↓
     GREEN

Coverage 3–7 days
        ↓
     AMBER

Coverage < 3 days
        ↓
      RED
```

These thresholds are configurable prototype values and are not official operational thresholds.

The system should present the underlying information so that users can understand why a requirement was flagged.

---

# 9. Step 7 — Requirement Prioritization

The system combines demand and risk information to create a structured priority view.

Possible inputs include:

```text
Forecast Demand
      +
Current Inventory
      +
Coverage
      +
Risk
      +
Planning Constraints
      ↓
Priority Information
```

The prioritization logic should be transparent and configurable.

Example output:

| Requirement   | Coverage | Risk  | Priority      |
| ------------- | -------: | ----- | ------------- |
| Requirement A |  10 days | Green | Review        |
| Requirement B |   5 days | Amber | Attention     |
| Requirement C |   2 days | Red   | Urgent Review |

These are illustrative examples only.

---

# 10. Step 8 — Route Optimization

After requirements are identified, the optimization module can generate candidate delivery plans.

Inputs can include:

* Delivery requirements
* Vehicle availability
* Vehicle capacity
* Route constraints
* Travel information
* Planning priorities

Conceptual flow:

```text
Priority Requirements
        ↓
Available Vehicles
        ↓
Constraints
        ↓
Optimization Solver
        ↓
Candidate Delivery Plan
        ↓
Constraint Validation
```

OR-Tools can be used for vehicle-routing and related optimization problems.

---

# 11. Step 9 — Command Dashboard

The dashboard presents the processed information to authorized users.

The dashboard can contain:

## Overview

* Total requirements
* Risk summary
* Forecast summary
* Inventory status

## Forecasting

* Historical demand
* Predicted demand
* Forecast trend
* Model evaluation

## Risk

* Risk indicators
* Coverage information
* Requirements requiring review

## Route Planning

* Candidate delivery plan
* Vehicle utilization
* Route constraints

## What-If Simulation

* Scenario parameters
* Scenario results
* Comparison with baseline

---

# 12. Step 10 — Human Review

RASAD-AI is designed as a decision-support system.

The generated information should be reviewed by an authorized human user.

The user can:

* Review forecast information
* Review risk indicators
* Review priorities
* Examine route proposals
* Run scenarios
* Modify planning assumptions
* Approve or reject a proposed plan

The system should not independently execute operational decisions.

---

# 13. Step 11 — Planning Output

After review, the system can produce structured planning information.

Possible outputs include:

```text
Forecast Summary
      +
Risk Summary
      +
Priority Requirements
      +
Candidate Delivery Plan
      ↓
Reviewed Planning Output
```

The final output should clearly distinguish between:

* System-generated recommendations
* User modifications
* Approved planning information

---

# 14. Step 12 — Feedback Loop

The system can use new authorized observations for evaluation.

```text
Planning
   ↓
Actual Consumption
   ↓
Observed Data
   ↓
Forecast Comparison
   ↓
Error Measurement
   ↓
Model Evaluation
   ↓
Future Model Improvement
```

This enables continuous testing and improvement.

---

# 15. What-If Workflow

The what-if simulator allows users to evaluate hypothetical scenarios.

## Scenario Workflow

```text
Current Planning State
        ↓
Select Scenario
        ↓
Change Assumption
        ↓
Recalculate Forecast / Risk
        ↓
Recalculate Planning
        ↓
Compare Results
        ↓
Human Review
```

Examples:

* Increased simulated demand
* Reduced inventory
* Changed vehicle capacity
* Simulated route unavailability
* Changed planning period

These scenarios are simulations and do not automatically change real-world systems.

---

# 16. Disruption Re-Planning Workflow

When a simulated or authorized route constraint changes, the planning process can be repeated.

```text
Existing Candidate Plan
        ↓
Constraint Change
        ↓
Affected Requirements
        ↓
Recalculate Feasible Options
        ↓
Optimization
        ↓
Alternative Candidate Plan
        ↓
Human Review
```

The purpose is to reduce the time required to evaluate alternative plans.

---

# 17. Error Handling

Each major component should provide appropriate error handling.

Examples:

### Data Error

```text
Invalid Data
    ↓
Validation Error
    ↓
Log Issue
    ↓
Request Correction
```

### Forecasting Error

```text
Model Failure
    ↓
Error Logging
    ↓
Fallback / Retry
    ↓
User Notification
```

### Optimization Error

```text
No Feasible Solution
    ↓
Constraint Analysis
    ↓
User Notification
    ↓
Parameter Review
```

The exact fallback strategy depends on the final implementation.

---

# 18. Security Workflow

Security should be applied throughout the workflow.

```text
User
 ↓
Authentication
 ↓
Authorization
 ↓
Role Validation
 ↓
API Request
 ↓
Business Logic
 ↓
Database
 ↓
Audit Log
```

The repository must not contain:

* Passwords
* API keys
* Private certificates
* Production credentials
* Classified information
* Restricted operational information

---

# 19. Prototype Data Workflow

The SIH prototype uses synthetic data.

```text
Synthetic Dataset
       ↓
Data Processing
       ↓
Forecast Model
       ↓
Risk Engine
       ↓
Optimization
       ↓
Dashboard
       ↓
Demo / Evaluation
```

This allows the technical concept to be demonstrated without using sensitive operational information.

---

# 20. End-to-End Example

The following is a simplified prototype example.

### Input

A simulated location has:

```text
Inventory = 500 units
Forecast Demand = 50 units/day
```

### Inventory Coverage

```text
500 / 50 = 10 days
```

### Risk

Using the prototype thresholds:

```text
10 days → GREEN
```

### New Scenario

Suppose the simulator changes the demand assumption:

```text
Demand = 100 units/day
```

Coverage becomes:

```text
500 / 100 = 5 days
```

The prototype risk category becomes:

```text
5 days → AMBER
```

The system can then recalculate the planning requirements and present the changed result to the authorized user.

This example is purely illustrative and uses synthetic values.

---

# 21. System Feedback Cycle

The complete system can be represented as:

```text
┌──────────────┐
│ Data         │
└──────┬───────┘
       ↓
┌──────────────┐
│ Forecast     │
└──────┬───────┘
       ↓
┌──────────────┐
│ Risk         │
└──────┬───────┘
       ↓
┌──────────────┐
│ Optimize     │
└──────┬───────┘
       ↓
┌──────────────┐
│ Dashboard    │
└──────┬───────┘
       ↓
┌──────────────┐
│ Human Review │
└──────┬───────┘
       ↓
┌──────────────┐
│ Planning     │
└──────┬───────┘
       ↓
┌──────────────┐
│ Actual Data  │
└──────┬───────┘
       │
       └──────────────→ Forecast Evaluation
```

---

# 22. Workflow Summary

RASAD-AI follows a structured pipeline:

1. Collect authorized or synthetic data.
2. Validate incoming records.
3. Clean and transform the data.
4. Generate demand forecasts.
5. Analyze inventory coverage.
6. Identify potential stock-out risks.
7. Prioritize requirements.
8. Generate candidate delivery plans.
9. Visualize results through the dashboard.
10. Allow authorized human review.
11. Produce structured planning information.
12. Use subsequent observations for model evaluation.

This workflow provides the foundation for integrating predictive analytics and optimization into a unified logistics decision-support platform.

---

## Important Note

This project is a prototype developed for Smart India Hackathon demonstration and academic evaluation.

All examples and datasets in the public repository should remain synthetic, simulated, or otherwise authorized.

The system is intended to demonstrate software architecture, predictive analytics, optimization, and decision-support capabilities and should not be interpreted as an operational military system.
