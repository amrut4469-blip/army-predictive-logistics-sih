# 🏗️ RASAD-AI — Solution Architecture

## 1. Overview

RASAD-AI is an AI-assisted predictive logistics and forward supply-chain decision-support platform.

The system combines:

* Data processing
* Demand forecasting
* Inventory analysis
* Stock-out risk assessment
* Requirement prioritization
* Route optimization
* What-if simulation
* Command-level visualization

The architecture is designed as a modular system so that forecasting, optimization, backend services, and the user interface can be developed and tested independently.

---

# 2. High-Level Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                          │
│                                                              │
│ Historical Consumption │ Inventory │ Personnel │ Weather    │
│ Route Status │ Vehicles │ Deliveries │ Other Authorized Data │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 DATA INGESTION & VALIDATION                  │
│                                                              │
│ • Data validation                                             │
│ • Missing-value handling                                      │
│ • Data normalization                                          │
│ • Duplicate detection                                         │
│ • Schema validation                                           │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                     DATA STORAGE                              │
│                                                              │
│                    PostgreSQL / PostGIS                       │
│                                                              │
│ Historical Data │ Inventory │ Locations │ Deliveries         │
│ Routes │ Forecasts │ Risk Results │ Audit Records            │
└───────────────┬───────────────────────────────┬───────────────┘
                │                               │
                ▼                               ▼
┌───────────────────────────────┐   ┌───────────────────────────┐
│     DEMAND FORECASTING        │   │     RISK ENGINE            │
│                               │   │                           │
│ Time-series / ML models       │   │ Inventory coverage        │
│ Historical trends             │   │ Forecast demand           │
│ Seasonality                   │   │ Stock-out risk             │
│ Other authorized features     │   │ Priority indicators        │
└───────────────┬───────────────┘   └──────────────┬────────────┘
                │                                  │
                └────────────────┬─────────────────┘
                                 ▼
┌──────────────────────────────────────────────────────────────┐
│                  REQUIREMENT PRIORITIZATION                   │
│                                                              │
│ Forecast Demand + Inventory + Risk + Constraints             │
│                         ↓                                    │
│                  Priority Requirements                        │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                   ROUTE OPTIMIZATION                         │
│                                                              │
│ Vehicle Capacity │ Delivery Requirements │ Route Constraints │
│                         ↓                                    │
│                Feasible Delivery Plan                        │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                         FASTAPI                              │
│                                                              │
│ REST APIs │ Authentication │ Business Logic │ WebSocket      │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                    COMMAND DASHBOARD                         │
│                                                              │
│ React │ Maps │ Forecast Charts │ Risk Indicators             │
│ Route Visualization │ What-If Simulator                      │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                  HUMAN REVIEW & APPROVAL                     │
│                                                              │
│ Authorized user reviews the generated decision-support       │
│ information before operational use.                          │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 ACTUAL CONSUMPTION / RESULTS                 │
│                                                              │
│ New observations can be used for future model evaluation     │
│ and improvement.                                             │
└──────────────────────────────────────────────────────────────┘
```

---

# 3. Architecture Layers

The system is divided into several logical layers.

---

## 3.1 Data Layer

The data layer stores information required for forecasting, inventory analysis, and planning.

Potential data categories include:

* Historical consumption
* Current inventory
* Supply categories
* Location information
* Authorized personnel information
* Vehicle information
* Delivery records
* Route status
* Weather information

For the prototype, synthetic data is used.

---

## 3.2 Data Processing Layer

The data processing layer converts raw input into a structured format suitable for analytics and machine learning.

Main responsibilities include:

### Validation

Check whether incoming records contain valid values and expected fields.

### Cleaning

Handle:

* Missing values
* Duplicate records
* Invalid values
* Inconsistent formats

### Transformation

Convert raw records into model-ready features.

### Aggregation

Create useful summaries such as:

* Daily consumption
* Weekly consumption
* Inventory coverage
* Historical demand trends

---

# 4. Demand Forecasting Layer

The forecasting layer estimates future requirements.

A generic forecasting workflow is:

```text
Historical Consumption
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Train / Validation Split
        ↓
Forecasting Model
        ↓
Future Demand Estimate
        ↓
Model Evaluation
```

Potential forecasting approaches include:

* Statistical time-series models
* Prophet
* XGBoost
* LSTM
* Other suitable forecasting models

The final model should be selected based on actual validation results and dataset characteristics.

---

# 5. Inventory & Risk Layer

The risk engine combines inventory information with forecast demand.

A simplified concept is:

```text
Current Inventory
       +
Forecast Demand
       ↓
Estimated Inventory Coverage
       ↓
Risk Assessment
```

A prototype can represent risk using configurable coverage thresholds.

Example:

```text
Coverage > 7 days       → GREEN
Coverage 3–7 days       → AMBER
Coverage < 3 days       → RED
```

These values are prototype configuration values and should not be interpreted as official operational thresholds.

---

# 6. Requirement Prioritization

After forecasting and risk assessment, the system creates a structured list of requirements.

Potential prioritization inputs include:

* Forecast demand
* Current inventory
* Estimated coverage
* Risk level
* Delivery requirements
* Vehicle/resource constraints

The output can be represented as:

```text
Requirement
     ↓
Risk Assessment
     ↓
Priority Calculation
     ↓
Planner Review
```

The prioritization mechanism should remain configurable and explainable.

---

# 7. Route Optimization Layer

The route optimization module assists with generating feasible delivery plans.

A simplified optimization workflow is:

```text
Delivery Requirements
        +
Vehicle Availability
        +
Vehicle Capacity
        +
Route Constraints
        ↓
Optimization Solver
        ↓
Candidate Delivery Plan
        ↓
Constraint Validation
        ↓
Planner Review
```

The project can use a vehicle-routing optimization approach such as OR-Tools.

The optimizer should be treated as a planning-support component rather than an autonomous decision-maker.

---

# 8. What-If Simulation Layer

The what-if simulator allows authorized users to evaluate hypothetical changes.

Example scenarios include:

### Scenario A — Increased Demand

```text
Demand
  +20%
   ↓
Forecast Recalculation
   ↓
Risk Recalculation
   ↓
New Planning Result
```

### Scenario B — Route Unavailable

```text
Selected Route
      ↓
Marked Unavailable
      ↓
Alternative Planning
      ↓
Updated Route Proposal
```

### Scenario C — Vehicle Capacity Change

```text
Vehicle Capacity
      ↓
Updated Constraint
      ↓
Optimization
      ↓
New Delivery Plan
```

The simulator is intended to support planning analysis without automatically executing any real-world action.

---

# 9. Backend Layer

The backend provides the application services required by the dashboard and analytical modules.

The proposed backend technology is:

* Python
* FastAPI
* PostgreSQL
* Redis
* Celery where background processing is required

Responsibilities include:

* API request handling
* Authentication and authorization
* Data access
* Forecast service integration
* Risk calculations
* Optimization service integration
* Scenario simulation
* Audit logging

---

# 10. API Layer

The API layer provides controlled communication between the frontend and backend services.

Conceptual flow:

```text
React Dashboard
       ↓
     HTTPS
       ↓
    FastAPI
       ↓
┌──────┼──────────┬───────────┐
↓      ↓          ↓           ↓
Data  Forecast   Risk      Optimization
       Service   Engine       Service
```

The exact API endpoints should correspond to the implemented backend.

If FastAPI is used, interactive API documentation can be exposed through the framework's standard documentation interface in development environments.

---

# 11. Frontend Layer

The frontend provides the primary user interface.

Proposed technologies:

* React
* JavaScript / TypeScript
* Charting library
* Mapping library
* Responsive UI components

The dashboard can provide:

### Overview

* System status
* Requirement summary
* Risk summary
* Forecast summary

### Forecast View

* Historical demand
* Predicted demand
* Forecast trend
* Model metrics

### Risk View

* Risk indicators
* Inventory coverage
* Requirements requiring attention

### Route View

* Delivery plan
* Route visualization
* Vehicle information
* Constraints

### What-If View

* Scenario configuration
* Scenario comparison
* Result visualization

---

# 12. Database Architecture

The prototype can use PostgreSQL for structured application data.

PostGIS may be used where spatial information is required.

Conceptual entities include:

```text
Users
  │
  ├── Roles
  │
  └── Audit Logs

Locations
  │
  ├── Inventory
  ├── Consumption
  ├── Forecasts
  └── Requirements

Vehicles
  │
  └── Delivery Plans

Routes
  │
  └── Route Constraints

Scenarios
  │
  └── Simulation Results
```

The exact schema should be documented separately in:

```text
docs/database-design.md
```

---

# 13. Security Architecture

Security should be considered across every layer.

```text
User
 ↓
Authentication
 ↓
Authorization / RBAC
 ↓
API
 ↓
Business Logic
 ↓
Database
```

Security measures may include:

* Authentication
* Role-based access control
* Secure API access
* Input validation
* Audit logging
* Encryption where appropriate
* Secure secret management
* Controlled deployment

No real credentials or secrets should be stored in the repository.

---

# 14. Offline / Controlled Deployment

The platform is designed with controlled deployment environments in mind.

Possible deployment environments include:

* Local development
* Private infrastructure
* On-premise deployment
* Controlled network environments

An offline-first or limited-connectivity architecture can reduce dependence on continuous external connectivity.

The exact deployment configuration depends on the final implementation.

---

# 15. Feedback Loop

The architecture supports a continuous analytical feedback loop.

```text
Forecast
   ↓
Planning
   ↓
Actual Consumption
   ↓
Observed Data
   ↓
Model Evaluation
   ↓
Model Improvement
   ↓
Updated Forecast
```

This enables the system to be evaluated and improved using newly available authorized data.

---

# 16. Technology Stack

| Layer           | Technology                            |
| --------------- | ------------------------------------- |
| Frontend        | React                                 |
| Maps            | Leaflet / compatible mapping solution |
| Backend         | Python + FastAPI                      |
| Database        | PostgreSQL                            |
| Spatial Data    | PostGIS                               |
| Cache / Queue   | Redis                                 |
| Background Jobs | Celery                                |
| Forecasting     | Statistical / ML models               |
| Optimization    | OR-Tools                              |
| Deployment      | Docker                                |
| Security        | RBAC, authentication, audit logging   |

The exact technology selection may evolve during implementation.

---

# 17. Deployment Architecture

A possible containerized deployment is:

```text
                    ┌───────────────────┐
                    │   User Browser    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ React Frontend    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   FastAPI Server  │
                    └───────┬─────┬─────┘
                            │     │
              ┌─────────────┘     └─────────────┐
              ▼                                 ▼
      ┌─────────────────┐              ┌─────────────────┐
      │ Forecast Engine │              │ Optimization    │
      │                 │              │ Engine           │
      └────────┬────────┘              └────────┬────────┘
               │                                │
               └──────────────┬─────────────────┘
                              ▼
                    ┌───────────────────┐
                    │ PostgreSQL/PostGIS│
                    └───────────────────┘
```

Docker can be used to package services consistently across development and deployment environments.

---

# 18. Design Principles

The architecture follows these principles:

### Modular

Each major component should have a defined responsibility.

### Explainable

Forecasts, risk indicators, and optimization results should be understandable to authorized users.

### Secure

Sensitive information should be protected through appropriate security controls.

### Human-in-the-Loop

The system provides decision support rather than autonomous operational control.

### Scalable

The architecture should allow additional locations, supply categories, and analytical modules to be introduced later.

### Testable

Individual modules should be independently testable.

### Data-Driven

Model and optimization decisions should be evaluated using measurable data and validation methods.

---

# 19. End-to-End Architecture Flow

The complete conceptual flow is:

```text
┌──────────────────────┐
│ Authorized Data      │
│ Sources              │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Data Processing      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Demand Forecasting   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Inventory Analysis   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Risk Assessment      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Prioritization       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Route Optimization   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ FastAPI Backend      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ React Dashboard      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Human Review         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Planning Output      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Feedback / Evaluation│
└──────────────────────┘
```

---

# 20. Architecture Summary

RASAD-AI integrates predictive analytics, inventory risk assessment, optimization, and visualization into a unified logistics decision-support platform.

The architecture separates:

* Data management
* Forecasting
* Risk analysis
* Optimization
* Backend services
* Frontend visualization
* Security
* Human review

This modular design makes the prototype easier to test, demonstrate, improve, and extend while keeping the system focused on responsible decision support.
