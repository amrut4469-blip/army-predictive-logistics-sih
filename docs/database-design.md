# 🗄️ RASAD-AI — Database Design

## 1. Overview

RASAD-AI uses a structured database architecture to manage the data required for predictive logistics planning.

The proposed database is designed around **PostgreSQL** with **PostGIS** support for spatial and location-based operations.

The database supports the following major functions:

* Supply and inventory management
* Historical consumption tracking
* Demand forecasting
* Stock-out risk assessment
* Requirement prioritization
* Vehicle and delivery planning
* Route optimization
* What-if scenario analysis
* Delivery tracking
* Audit logging
* Dashboard reporting

> **Important:** This document describes the proposed/prototype database design. The exact schema should be updated to match the final implemented backend when development progresses.

---

# 2. Database Objectives

The database should provide:

1. Reliable storage of logistics data
2. Efficient retrieval of historical consumption
3. Support for time-series forecasting
4. Inventory and stock monitoring
5. Risk assessment storage
6. Requirement prioritization
7. Route and vehicle planning
8. Scenario simulation
9. Auditability
10. Secure role-based access
11. Spatial queries using PostGIS
12. Compatibility with offline or controlled deployment environments

---

# 3. Proposed Technology

| Component            | Technology                      |
| -------------------- | ------------------------------- |
| Database             | PostgreSQL                      |
| Spatial Extension    | PostGIS                         |
| Backend              | FastAPI                         |
| ORM / Database Layer | SQLAlchemy or equivalent        |
| API Format           | REST / JSON                     |
| Authentication       | Role-based authentication       |
| Visualization        | React + Leaflet                 |
| Optimization         | OR-Tools                        |
| AI/ML                | Python ML ecosystem             |
| Deployment           | Docker / controlled environment |

---

# 4. High-Level Database Architecture

```text
                         ┌──────────────────────┐
                         │      Users / Roles    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    FastAPI Backend   │
                         └──────────┬───────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
       ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
       │  Inventory  │       │ Consumption │       │ Locations   │
       └──────┬──────┘       └──────┬──────┘       └──────┬──────┘
              │                     │                     │
              └─────────────────────┼─────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Demand Forecasts     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Risk Assessments     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Requirements         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Delivery Planning    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Route Optimization   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Dashboard / Reports  │
                         └──────────────────────┘
```

---

# 5. Core Entities

The proposed database contains the following major entities:

| Entity              | Purpose                        |
| ------------------- | ------------------------------ |
| `users`             | Application users              |
| `roles`             | User access roles              |
| `locations`         | Logistics locations            |
| `supply_categories` | Supply classification          |
| `inventory`         | Current inventory levels       |
| `consumption`       | Historical consumption         |
| `forecasts`         | Predicted future demand        |
| `risk_assessments`  | Stock-out and supply risk      |
| `requirements`      | Supply requirements            |
| `vehicles`          | Delivery vehicle information   |
| `routes`            | Planned routes                 |
| `route_constraints` | Route restrictions/constraints |
| `delivery_plans`    | Delivery planning information  |
| `deliveries`        | Delivery records               |
| `scenarios`         | What-if scenarios              |
| `scenario_results`  | Simulation results             |
| `audit_logs`        | System activity history        |

---

# 6. Users Table

## Table: `users`

Stores application user information.

### Proposed Fields

| Column          | Type      | Description        |
| --------------- | --------- | ------------------ |
| `id`            | UUID      | Primary key        |
| `username`      | VARCHAR   | Unique username    |
| `email`         | VARCHAR   | User email         |
| `password_hash` | TEXT      | Hashed password    |
| `role_id`       | UUID      | Reference to roles |
| `is_active`     | BOOLEAN   | Account status     |
| `created_at`    | TIMESTAMP | Creation time      |
| `updated_at`    | TIMESTAMP | Last update        |

### Primary Key

```text
users.id
```

### Relationship

```text
users.role_id → roles.id
```

---

# 7. Roles Table

## Table: `roles`

Defines application access levels.

Possible prototype roles include:

* Administrator
* Planner
* Analyst
* Viewer

The exact role structure should be determined by the final application implementation.

### Proposed Fields

| Column        | Type      | Description      |
| ------------- | --------- | ---------------- |
| `id`          | UUID      | Primary key      |
| `name`        | VARCHAR   | Role name        |
| `description` | TEXT      | Role description |
| `created_at`  | TIMESTAMP | Creation time    |

---

# 8. Locations Table

## Table: `locations`

Stores geographic information required for logistics planning.

### Proposed Fields

| Column          | Type               | Description           |
| --------------- | ------------------ | --------------------- |
| `id`            | UUID               | Primary key           |
| `name`          | VARCHAR            | Location name         |
| `location_type` | VARCHAR            | Location category     |
| `latitude`      | DOUBLE             | Latitude              |
| `longitude`     | DOUBLE             | Longitude             |
| `geometry`      | GEOGRAPHY/GEOMETRY | PostGIS spatial field |
| `is_active`     | BOOLEAN            | Location status       |
| `created_at`    | TIMESTAMP          | Creation time         |

---

# 9. PostGIS Integration

PostGIS can be used to support geographic operations.

Example spatial field:

```text
geometry POINT
```

Conceptually:

```text
Location
   │
   ├── Latitude
   ├── Longitude
   └── Spatial Geometry
```

Possible spatial operations include:

* Distance calculations
* Location proximity analysis
* Geographic visualization
* Spatial filtering
* Route-related geographic processing

> The prototype should use only synthetic or authorized non-sensitive geographic data.

---

# 10. Supply Categories Table

## Table: `supply_categories`

Stores different supply categories handled by the system.

Examples for prototype data:

* Food / Rations
* Fuel
* Medical Supplies
* General Supplies

Other categories can be added according to the application requirements.

### Proposed Fields

| Column        | Type      | Description          |
| ------------- | --------- | -------------------- |
| `id`          | UUID      | Primary key          |
| `name`        | VARCHAR   | Category name        |
| `unit`        | VARCHAR   | Measurement unit     |
| `description` | TEXT      | Category description |
| `created_at`  | TIMESTAMP | Creation time        |

---

# 11. Inventory Table

## Table: `inventory`

Stores current stock information.

### Proposed Fields

| Column          | Type      | Description             |
| --------------- | --------- | ----------------------- |
| `id`            | UUID      | Primary key             |
| `location_id`   | UUID      | Storage location        |
| `category_id`   | UUID      | Supply category         |
| `item_name`     | VARCHAR   | Item identifier         |
| `quantity`      | DECIMAL   | Current quantity        |
| `minimum_level` | DECIMAL   | Minimum stock threshold |
| `maximum_level` | DECIMAL   | Maximum stock threshold |
| `unit`          | VARCHAR   | Measurement unit        |
| `updated_at`    | TIMESTAMP | Last update             |

### Relationships

```text
inventory.location_id
        ↓
locations.id

inventory.category_id
        ↓
supply_categories.id
```

---

# 12. Consumption Table

## Table: `consumption`

Stores historical consumption information.

This table is an important input for demand forecasting.

### Proposed Fields

| Column              | Type      | Description          |
| ------------------- | --------- | -------------------- |
| `id`                | UUID      | Primary key          |
| `location_id`       | UUID      | Location             |
| `category_id`       | UUID      | Supply category      |
| `item_name`         | VARCHAR   | Item                 |
| `consumption_date`  | DATE      | Consumption date     |
| `quantity_consumed` | DECIMAL   | Quantity consumed    |
| `unit`              | VARCHAR   | Measurement unit     |
| `created_at`        | TIMESTAMP | Record creation time |

---

# 13. Forecasts Table

## Table: `forecasts`

Stores demand forecasting results generated by the AI/ML pipeline.

### Proposed Fields

| Column               | Type      | Description                |
| -------------------- | --------- | -------------------------- |
| `id`                 | UUID      | Primary key                |
| `location_id`        | UUID      | Target location            |
| `category_id`        | UUID      | Supply category            |
| `forecast_date`      | DATE      | Forecast period            |
| `predicted_quantity` | DECIMAL   | Predicted demand           |
| `lower_bound`        | DECIMAL   | Lower uncertainty estimate |
| `upper_bound`        | DECIMAL   | Upper uncertainty estimate |
| `model_name`         | VARCHAR   | Model used                 |
| `model_version`      | VARCHAR   | Model version              |
| `created_at`         | TIMESTAMP | Forecast creation time     |

---

# 14. Risk Assessments Table

## Table: `risk_assessments`

Stores calculated supply and stock-out risk information.

### Proposed Fields

| Column                    | Type      | Description              |
| ------------------------- | --------- | ------------------------ |
| `id`                      | UUID      | Primary key              |
| `location_id`             | UUID      | Location                 |
| `category_id`             | UUID      | Supply category          |
| `risk_score`              | DECIMAL   | Calculated risk value    |
| `risk_level`              | VARCHAR   | Risk classification      |
| `estimated_stockout_date` | DATE      | Estimated stock-out date |
| `forecast_reference_id`   | UUID      | Related forecast         |
| `created_at`              | TIMESTAMP | Assessment time          |

The risk score should be treated as a **decision-support indicator**, not an automatic command.

---

# 15. Requirements Table

## Table: `requirements`

Stores supply requirements identified by the system or entered by an authorized user.

### Proposed Fields

| Column              | Type      | Description           |
| ------------------- | --------- | --------------------- |
| `id`                | UUID      | Primary key           |
| `location_id`       | UUID      | Destination           |
| `category_id`       | UUID      | Supply category       |
| `required_quantity` | DECIMAL   | Required quantity     |
| `priority`          | INTEGER   | Planning priority     |
| `required_by`       | TIMESTAMP | Required-by time      |
| `status`            | VARCHAR   | Requirement status    |
| `source`            | VARCHAR   | Source of requirement |
| `created_at`        | TIMESTAMP | Creation time         |

---

# 16. Vehicles Table

## Table: `vehicles`

Stores generic vehicle information required by the route optimization prototype.

### Proposed Fields

| Column                | Type      | Description        |
| --------------------- | --------- | ------------------ |
| `id`                  | UUID      | Primary key        |
| `vehicle_code`        | VARCHAR   | Vehicle identifier |
| `vehicle_type`        | VARCHAR   | Vehicle category   |
| `capacity`            | DECIMAL   | Maximum capacity   |
| `unit`                | VARCHAR   | Capacity unit      |
| `availability_status` | VARCHAR   | Availability       |
| `created_at`          | TIMESTAMP | Creation time      |

Only non-sensitive, synthetic vehicle identifiers should be used in the public prototype repository.

---

# 17. Routes Table

## Table: `routes`

Stores optimized route results.

### Proposed Fields

| Column                | Type      | Description          |
| --------------------- | --------- | -------------------- |
| `id`                  | UUID      | Primary key          |
| `vehicle_id`          | UUID      | Assigned vehicle     |
| `route_date`          | DATE      | Planned date         |
| `total_distance`      | DECIMAL   | Total route distance |
| `estimated_duration`  | INTEGER   | Estimated duration   |
| `total_load`          | DECIMAL   | Planned load         |
| `optimization_status` | VARCHAR   | Optimization status  |
| `created_at`          | TIMESTAMP | Creation time        |

---

# 18. Route Constraints Table

## Table: `route_constraints`

Stores generic planning constraints.

### Proposed Fields

| Column             | Type      | Description            |
| ------------------ | --------- | ---------------------- |
| `id`               | UUID      | Primary key            |
| `route_id`         | UUID      | Related route          |
| `constraint_type`  | VARCHAR   | Constraint type        |
| `constraint_value` | TEXT      | Constraint information |
| `is_active`        | BOOLEAN   | Constraint status      |
| `created_at`       | TIMESTAMP | Creation time          |

Examples of prototype constraints:

* Vehicle capacity
* Maximum route duration
* Delivery time window
* Location availability
* Priority requirements

---

# 19. Delivery Plans Table

## Table: `delivery_plans`

Stores finalized or proposed delivery planning information.

### Proposed Fields

| Column                | Type      | Description            |
| --------------------- | --------- | ---------------------- |
| `id`                  | UUID      | Primary key            |
| `planning_date`       | DATE      | Planning date          |
| `status`              | VARCHAR   | Plan status            |
| `generated_by`        | UUID      | User/system reference  |
| `optimization_run_id` | UUID      | Optimization reference |
| `created_at`          | TIMESTAMP | Creation time          |
| `updated_at`          | TIMESTAMP | Last update            |

---

# 20. Deliveries Table

## Table: `deliveries`

Stores delivery-level information.

### Proposed Fields

| Column             | Type      | Description           |
| ------------------ | --------- | --------------------- |
| `id`               | UUID      | Primary key           |
| `delivery_plan_id` | UUID      | Delivery plan         |
| `route_id`         | UUID      | Related route         |
| `requirement_id`   | UUID      | Related requirement   |
| `quantity`         | DECIMAL   | Planned quantity      |
| `status`           | VARCHAR   | Delivery status       |
| `planned_time`     | TIMESTAMP | Planned delivery time |
| `completed_time`   | TIMESTAMP | Completion time       |
| `created_at`       | TIMESTAMP | Creation time         |

---

# 21. Scenarios Table

## Table: `scenarios`

Stores what-if simulation inputs.

The scenario engine allows planners to test changes before accepting a plan.

### Proposed Fields

| Column        | Type      | Description          |
| ------------- | --------- | -------------------- |
| `id`          | UUID      | Primary key          |
| `name`        | VARCHAR   | Scenario name        |
| `description` | TEXT      | Scenario description |
| `created_by`  | UUID      | User                 |
| `status`      | VARCHAR   | Scenario status      |
| `created_at`  | TIMESTAMP | Creation time        |

Example prototype scenarios:

```text
Normal planning
Reduced vehicle availability
Increased demand
Temporary route restriction
Delayed delivery
Supply shortage
```

These scenarios should use synthetic data in the public prototype.

---

# 22. Scenario Results Table

## Table: `scenario_results`

Stores outputs generated by the simulation engine.

### Proposed Fields

| Column           | Type      | Description          |
| ---------------- | --------- | -------------------- |
| `id`             | UUID      | Primary key          |
| `scenario_id`    | UUID      | Scenario             |
| `metric_name`    | VARCHAR   | Metric               |
| `baseline_value` | DECIMAL   | Baseline value       |
| `scenario_value` | DECIMAL   | Scenario value       |
| `difference`     | DECIMAL   | Difference           |
| `created_at`     | TIMESTAMP | Result creation time |

---

# 23. Audit Logs Table

## Table: `audit_logs`

Stores important application activity for traceability.

### Proposed Fields

| Column        | Type      | Description                          |
| ------------- | --------- | ------------------------------------ |
| `id`          | UUID      | Primary key                          |
| `user_id`     | UUID      | User                                 |
| `action`      | VARCHAR   | Action performed                     |
| `entity_type` | VARCHAR   | Affected entity                      |
| `entity_id`   | UUID      | Affected record                      |
| `timestamp`   | TIMESTAMP | Action time                          |
| `metadata`    | JSONB     | Additional non-sensitive information |

Audit logging can help identify:

* Configuration changes
* Planning actions
* Scenario creation
* Forecast generation
* Route optimization requests
* Administrative actions

---

# 24. Entity Relationship Overview

```text
                    ┌──────────────┐
                    │    Roles     │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Users     │
                    └──────┬───────┘
                           │
             ┌─────────────┼──────────────┐
             │             │              │
             ▼             ▼              ▼
       ┌──────────┐  ┌────────────┐  ┌──────────────┐
       │ Scenarios│  │ Audit Logs │  │Delivery Plans│
       └────┬─────┘  └────────────┘  └──────┬───────┘
            │                                │
            ▼                                ▼
     ┌──────────────┐                  ┌────────────┐
     │Scenario      │                  │ Deliveries │
     │Results       │                  └─────┬──────┘
     └──────────────┘                        │
                                            ▼
                                      ┌────────────┐
                                      │   Routes   │
                                      └─────┬──────┘
                                            │
                                            ▼
                                      ┌────────────┐
                                      │  Vehicles  │
                                      └────────────┘


 ┌─────────────┐       ┌──────────────────┐
 │  Locations  │──────▶│    Inventory     │
 └──────┬──────┘       └────────┬─────────┘
        │                        │
        │                        ▼
        │                ┌──────────────────┐
        │                │   Consumption   │
        │                └────────┬─────────┘
        │                         │
        │                         ▼
        │                ┌──────────────────┐
        │                │    Forecasts     │
        │                └────────┬─────────┘
        │                         │
        │                         ▼
        │                ┌──────────────────┐
        └───────────────▶│ Risk Assessments │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Requirements   │
                         └──────────────────┘

```

---

# 25. Main Relationships

The primary relationships are:

```text
roles
  │
  └── users

locations
  │
  ├── inventory
  ├── consumption
  ├── forecasts
  ├── risk_assessments
  └── requirements

supply_categories
  │
  ├── inventory
  ├── consumption
  ├── forecasts
  ├── risk_assessments
  └── requirements

vehicles
  │
  └── routes

routes
  │
  ├── route_constraints
  └── deliveries

delivery_plans
  │
  └── deliveries

requirements
  │
  └── deliveries

scenarios
  │
  └── scenario_results

users
  │
  ├── scenarios
  └── audit_logs
```

---

# 26. Indexing Strategy

Indexes should be created for frequently queried fields.

Potential indexes include:

```text
users.email
users.role_id

locations.location_type
locations.geometry

inventory.location_id
inventory.category_id

consumption.location_id
consumption.category_id
consumption.consumption_date

forecasts.location_id
forecasts.category_id
forecasts.forecast_date

risk_assessments.location_id
risk_assessments.category_id
risk_assessments.risk_level

requirements.location_id
requirements.priority
requirements.required_by

routes.vehicle_id
routes.route_date

deliveries.delivery_plan_id
deliveries.route_id
deliveries.status

audit_logs.user_id
audit_logs.timestamp
```

Time-series queries should be designed carefully because historical consumption and forecasting data can grow significantly.

---

# 27. Data Validation

The backend should validate incoming data before storing it.

Examples:

```text
Quantity >= 0
Capacity > 0
Latitude within valid geographic range
Longitude within valid geographic range
Required date is valid
Priority belongs to an accepted range
Foreign-key references exist
Required fields are not null
```

Invalid records should be rejected or flagged for correction.

---

# 28. Data Lifecycle

The proposed data lifecycle is:

```text
Data Input
    ↓
Validation
    ↓
Normalization
    ↓
Database Storage
    ↓
AI/ML Processing
    ↓
Risk Analysis
    ↓
Optimization
    ↓
Dashboard
    ↓
Human Review
    ↓
Planning Decision
    ↓
Feedback / Historical Record
```

---

# 29. Forecasting Data Flow

```text
Historical Consumption
          │
          ▼
      PostgreSQL
          │
          ▼
   Data Preparation
          │
          ▼
    Feature Engineering
          │
          ▼
      ML Model
          │
          ▼
      Forecast
          │
          ▼
     forecasts
          │
          ▼
   Risk Assessment
```

---

# 30. Inventory and Risk Data Flow

```text
Current Inventory
       │
       ├──────────────┐
       │              │
       ▼              ▼
Historical       Forecast
Consumption      Demand
       │              │
       └──────┬───────┘
              ▼
       Risk Calculation
              │
              ▼
       risk_assessments
              │
              ▼
        Requirements
```

---

# 31. Route Planning Data Flow

```text
Requirements
     │
     ├── Quantity
     ├── Priority
     └── Destination
            │
            ▼
       Delivery Plan
            │
            ▼
         Vehicles
            │
            ▼
    Route Optimization
            │
            ▼
          Routes
            │
            ▼
        Deliveries
```

---

# 32. What-If Simulation Data Flow

```text
Current Planning State
          │
          ▼
     Create Scenario
          │
          ▼
 Modify Selected Inputs
          │
          ▼
 Run Forecast / Risk / Optimization
          │
          ▼
     Scenario Results
          │
          ▼
 Compare With Baseline
          │
          ▼
     Human Review
```

The simulation should not automatically change the operational baseline plan.

---

# 33. Database Security

The database should follow secure development practices.

Recommended controls include:

* Strong authentication
* Role-based authorization
* Password hashing
* Parameterized queries
* ORM/query validation
* Database access restrictions
* Encryption where appropriate
* Secure environment variables
* Audit logging
* Regular backups
* Least-privilege database accounts

Credentials must never be committed to GitHub.

---

# 34. Environment Configuration

Database credentials should be stored outside source code.

Example:

```text
DATABASE_URL=<environment-specific-value>
```

The actual value must not be committed.

For local development, use an environment file such as:

```text
.env
```

and keep it excluded through `.gitignore`.

A safe example file can be provided as:

```text
.env.example
```

without real credentials.

---

# 35. Synthetic Data Policy

The public GitHub repository must use:

* Synthetic data
* Publicly available non-sensitive data
* Artificial identifiers
* Demonstration locations
* Simulated inventory
* Simulated consumption
* Simulated vehicle data

The repository must not contain:

* Classified information
* Operationally sensitive logistics information
* Real restricted routes
* Sensitive military locations
* Real operational schedules
* Real personnel information
* Real credentials
* Secrets or API keys

---

# 36. Backup and Recovery

A production-quality deployment should consider:

```text
Primary Database
       │
       ▼
Scheduled Backup
       │
       ▼
Secure Backup Storage
       │
       ▼
Recovery Testing
```

Backup frequency and retention should be determined according to the deployment environment and applicable security requirements.

The public prototype does not claim production-level disaster recovery capability unless implemented and tested.

---

# 37. API and Database Interaction

The FastAPI backend acts as the primary application layer.

```text
React Dashboard
       │
       │ REST API
       ▼
FastAPI Backend
       │
       ├── Authentication
       ├── Validation
       ├── Business Logic
       ├── Forecast Service
       ├── Risk Engine
       └── Optimization Service
       │
       ▼
PostgreSQL / PostGIS
```

The frontend should not directly connect to the database.

---

# 38. Example Data Flow

An illustrative prototype flow:

```text
Consumption Data
       ↓
Database
       ↓
Forecast Model
       ↓
Predicted Demand
       ↓
Risk Engine
       ↓
Priority Requirement
       ↓
Route Optimizer
       ↓
Delivery Plan
       ↓
Dashboard
```

This demonstrates how the database acts as the central data layer connecting different RASAD-AI components.

---

# 39. Database Performance Considerations

Potential performance improvements include:

* Proper indexing
* Query optimization
* Pagination
* Connection pooling
* Batch processing
* Historical data partitioning where appropriate
* Efficient spatial indexes
* Caching frequently accessed non-sensitive results

Performance should be measured using representative synthetic datasets.

---

# 40. Data Consistency

The system should maintain consistency between related entities.

For example:

```text
Requirement
     │
     └── Delivery
            │
            └── Route
                   │
                   └── Vehicle
```

Foreign-key constraints should be used where appropriate.

Transactions should be used for operations that update multiple related records.

---

# 41. Auditability

Important planning and system actions should generate audit records.

Example:

```text
User
  ↓
Action
  ↓
Entity
  ↓
Timestamp
  ↓
Audit Log
```

This supports:

* Traceability
* Debugging
* Accountability
* Security monitoring
* Reproducibility of prototype decisions

---

# 42. Human-in-the-Loop Principle

The database stores recommendations and planning outputs, but the system should not be presented as an autonomous decision-maker.

The intended flow is:

```text
AI/Optimization
       ↓
Recommendation
       ↓
Human Review
       ↓
Approval / Modification
       ↓
Final Planning Decision
```

This principle is important for responsible use of predictive analytics and optimization systems.

---

# 43. Prototype vs Production

The database architecture is designed as a scalable prototype foundation.

### Prototype

The prototype may include:

* PostgreSQL
* Synthetic datasets
* Basic PostGIS support
* Forecast storage
* Risk storage
* Route optimization results
* Scenario simulation
* Dashboard integration

### Future Production Architecture

A production deployment may additionally require:

* Hardened infrastructure
* Stronger authentication
* Advanced access controls
* High availability
* Backup and recovery procedures
* Security monitoring
* Data governance
* Formal validation
* Deployment-specific compliance controls

These capabilities should not be claimed unless actually implemented and tested.

---

# 44. Suggested Database Module Structure

A possible backend structure is:

```text
src/
├── database/
│   ├── connection.py
│   ├── models/
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── location.py
│   │   ├── inventory.py
│   │   ├── consumption.py
│   │   ├── forecast.py
│   │   ├── risk.py
│   │   ├── requirement.py
│   │   ├── vehicle.py
│   │   ├── route.py
│   │   ├── delivery.py
│   │   ├── scenario.py
│   │   └── audit_log.py
│   │
│   ├── schemas/
│   │   ├── inventory.py
│   │   ├── forecast.py
│   │   ├── requirement.py
│   │   └── delivery.py
│   │
│   └── migrations/
│
├── api/
├── services/
├── ml/
└── optimization/
```

The actual project structure should be updated to match the implementation.

---

# 45. Database Integration With RASAD-AI

The database connects the major components of RASAD-AI:

```text
             ┌───────────────────────┐
             │     Data Sources      │
             └───────────┬───────────┘
                         │
                         ▼
             ┌───────────────────────┐
             │      PostgreSQL       │
             │       + PostGIS       │
             └───────────┬───────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   Forecasting       Risk Engine      Optimization
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   FastAPI API   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ React Dashboard  │
                └─────────────────┘
```

---

# 46. Database Design Principles

The database design follows these principles:

### 1. Modularity

Each major domain is represented separately.

### 2. Integrity

Foreign keys and validation rules help maintain consistent data.

### 3. Scalability

The design allows additional supply categories, locations, models and scenarios.

### 4. Security

Sensitive configuration and credentials remain outside source code.

### 5. Auditability

Important actions can be recorded through audit logs.

### 6. Spatial Awareness

PostGIS can support geographic analysis.

### 7. AI Integration

Forecast outputs can be stored and connected to downstream risk and planning components.

### 8. Human Oversight

Database records support recommendations and planning workflows without replacing human decision-making.

---

# 47. Current Prototype Status

The database design should clearly distinguish between implemented and proposed functionality.

| Component               | Status               |
| ----------------------- | -------------------- |
| PostgreSQL architecture | Proposed / Prototype |
| PostGIS support         | Proposed / Prototype |
| Inventory schema        | Proposed             |
| Consumption schema      | Proposed             |
| Forecast schema         | Proposed             |
| Risk schema             | Proposed             |
| Requirements schema     | Proposed             |
| Vehicle schema          | Proposed             |
| Route schema            | Proposed             |
| Delivery schema         | Proposed             |
| Scenario schema         | Proposed             |
| Audit logging           | Proposed             |
| Production hardening    | Future               |

The table should be updated as implementation progresses.

---

# 48. Future Database Enhancements

Potential future improvements include:

* Advanced time-series storage
* Partitioned historical consumption tables
* Improved spatial indexing
* Materialized reporting views
* Database-level monitoring
* Advanced audit systems
* Data versioning
* Model metadata storage
* Forecast lineage tracking
* Scenario comparison storage
* Automated data-quality checks
* Backup verification
* High-availability deployment

---

# 49. Summary

The proposed RASAD-AI database architecture provides a structured foundation for predictive logistics planning.

It connects:

```text
Historical Data
      ↓
Inventory
      ↓
Consumption
      ↓
Forecasting
      ↓
Risk Assessment
      ↓
Requirements
      ↓
Route Optimization
      ↓
Delivery Planning
      ↓
Dashboard
      ↓
Human Review
```

PostgreSQL provides structured relational storage while PostGIS can support geographic operations.

The database is designed to support the RASAD-AI prototype while leaving room for future scalability and controlled deployment.

> **Responsible-use note:** The public project is intended for demonstration, research and prototype evaluation using synthetic or authorized non-sensitive data. It must not contain classified, restricted or operationally sensitive military information.

---

## 50. Document Status

**Project:** RASAD-AI
**Problem Statement:** SIH26251
**Document:** Database Design
**Status:** Prototype / Proposed Architecture
**Data Classification:** Synthetic / Non-Sensitive Demonstration Data
**Last Updated:** 2026
