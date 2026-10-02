# 🔌 RASAD-AI — API Documentation

## 1. Overview

RASAD-AI uses a backend API layer to connect the React dashboard with the forecasting, inventory, risk assessment, scenario simulation and route optimization components.

The proposed backend architecture uses **FastAPI** with REST-style endpoints.

```text
React Dashboard
       │
       │ HTTP / JSON
       ▼
┌─────────────────────┐
│     FastAPI API     │
└──────────┬──────────┘
           │
     ┌─────┼─────────────┐
     │     │             │
     ▼     ▼             ▼
 Database  AI/ML     Optimization
           Services      Engine
```

> **Implementation note:** The endpoint structure below represents the proposed/prototype API design. Endpoint names and request/response schemas should be updated to exactly match the final implementation.

---

# 2. API Objectives

The API layer is responsible for:

* User authentication
* Inventory management
* Consumption data access
* Demand forecasting
* Risk assessment
* Requirement management
* Route optimization
* Delivery planning
* What-if simulation
* Dashboard data
* Audit information

The API provides a controlled interface between the frontend and backend services.

---

# 3. Technology Stack

| Component            | Technology          |
| -------------------- | ------------------- |
| Backend Framework    | FastAPI             |
| Programming Language | Python              |
| API Style            | REST                |
| Data Format          | JSON                |
| Database             | PostgreSQL          |
| Spatial Database     | PostGIS             |
| AI/ML                | Python ML ecosystem |
| Optimization         | OR-Tools            |
| Frontend             | React               |
| API Documentation    | OpenAPI / Swagger   |
| Containerization     | Docker              |

---

# 4. Base URL

For local development, an example base URL is:

```text
http://localhost:8000
```

A deployed environment should use its environment-specific secure URL.

Example:

```text
https://<deployment-domain>/api
```

The actual production URL should not be committed until the deployment exists.

---

# 5. API Documentation Interface

FastAPI can automatically generate interactive API documentation.

Typical development endpoints are:

```text
/docs
/redoc
/openapi.json
```

These endpoints allow developers to inspect available APIs and their request/response schemas.

---

# 6. API Architecture

```text
                     ┌────────────────────┐
                     │   React Dashboard   │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │    API Gateway     │
                     │     / FastAPI      │
                     └─────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
   Authentication        Business Logic        Validation
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
       PostgreSQL          AI/ML Service      Optimization
          + PostGIS                             Service
```

---

# 7. API Versioning

The API should support versioning to make future changes easier.

Recommended pattern:

```text
/api/v1/
```

Example:

```text
/api/v1/inventory
/api/v1/forecasts
/api/v1/risk
/api/v1/routes
```

Future versions can use:

```text
/api/v2/
```

This avoids breaking existing clients when the API evolves.

---

# 8. Authentication

Protected endpoints should require authenticated access.

A typical flow is:

```text
User
 │
 ▼
Login
 │
 ▼
Authentication Service
 │
 ▼
Access Token
 │
 ▼
API Request
 │
 ▼
Authorization Check
 │
 ▼
Protected Endpoint
```

The final authentication mechanism should be selected according to the deployment environment.

Possible approaches include:

* JWT-based authentication
* Secure session authentication
* Deployment-specific identity provider

---

# 9. Authorization

Authentication identifies the user.

Authorization determines what the user is allowed to access.

Example roles:

```text
Administrator
Planner
Analyst
Viewer
```

The actual roles should match the implemented access-control system.

Example conceptual permissions:

| Role          | Dashboard | Forecast | Optimization | Administration |
| ------------- | --------: | -------: | -----------: | -------------: |
| Administrator |       Yes |      Yes |          Yes |            Yes |
| Planner       |       Yes |      Yes |          Yes |        Limited |
| Analyst       |       Yes |      Yes |         View |             No |
| Viewer        |       Yes |     View |         View |             No |

This table is an example design and should be updated according to the final implementation.

---

# 10. Standard HTTP Methods

The API follows common REST conventions.

| Method   | Purpose                        |
| -------- | ------------------------------ |
| `GET`    | Retrieve information           |
| `POST`   | Create or execute an operation |
| `PUT`    | Replace/update a resource      |
| `PATCH`  | Partially update a resource    |
| `DELETE` | Remove a resource              |

---

# 11. Standard Response Format

A successful response can follow a consistent structure.

Example:

```json
{
  "success": true,
  "data": {},
  "message": "Request completed successfully"
}
```

An error response can use:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request data"
  }
}
```

The exact response format should match the final backend implementation.

---

# 12. HTTP Status Codes

Common status codes:

| Status | Meaning                                  |
| ------ | ---------------------------------------- |
| `200`  | Successful request                       |
| `201`  | Resource created                         |
| `204`  | Successful request with no response body |
| `400`  | Invalid request                          |
| `401`  | Authentication required                  |
| `403`  | Access denied                            |
| `404`  | Resource not found                       |
| `409`  | Conflict                                 |
| `422`  | Validation error                         |
| `429`  | Rate limit exceeded                      |
| `500`  | Internal server error                    |
| `503`  | Service unavailable                      |

---

# 13. Authentication Endpoints

## POST `/api/v1/auth/login`

Authenticates a user.

### Request

```json
{
  "username": "demo_user",
  "password": "example-password"
}
```

### Response

```json
{
  "success": true,
  "data": {
    "access_token": "<token>",
    "token_type": "bearer"
  }
}
```

The example credentials are placeholders only.

No real credentials should be stored in the repository.

---

## GET `/api/v1/auth/me`

Returns information about the currently authenticated user.

### Example Response

```json
{
  "success": true,
  "data": {
    "id": "user-demo-001",
    "username": "demo_user",
    "role": "planner"
  }
}
```

---

# 14. Dashboard API

## GET `/api/v1/dashboard/summary`

Returns high-level dashboard information.

### Example Response

```json
{
  "success": true,
  "data": {
    "inventory_items": 120,
    "active_requirements": 18,
    "high_risk_items": 5,
    "planned_routes": 8,
    "active_scenarios": 2
  }
}
```

These values are illustrative.

---

## GET `/api/v1/dashboard/risk-summary`

Returns aggregated risk information for dashboard visualization.

### Example Response

```json
{
  "success": true,
  "data": {
    "low": 35,
    "medium": 14,
    "high": 5
  }
}
```

---

# 15. Locations API

## GET `/api/v1/locations`

Returns available locations.

### Example Response

```json
{
  "success": true,
  "data": [
    {
      "id": "loc-001",
      "name": "Demo Location A",
      "latitude": 18.5204,
      "longitude": 73.8567,
      "type": "storage"
    }
  ]
}
```

Only synthetic or authorized non-sensitive location data should be used in the public prototype.

---

## GET `/api/v1/locations/{location_id}`

Returns details for a specific location.

Example:

```text
/api/v1/locations/loc-001
```

---

# 16. Inventory API

## GET `/api/v1/inventory`

Returns inventory records.

Optional query parameters may include:

```text
location_id
category_id
status
page
limit
```

Example:

```text
/api/v1/inventory?location_id=loc-001
```

---

## GET `/api/v1/inventory/{inventory_id}`

Returns a specific inventory record.

---

## POST `/api/v1/inventory`

Creates an inventory record.

### Example Request

```json
{
  "location_id": "loc-001",
  "category_id": "food",
  "item_name": "Demo Supply",
  "quantity": 1000,
  "unit": "units",
  "minimum_level": 250
}
```

---

## PATCH `/api/v1/inventory/{inventory_id}`

Updates inventory information.

Example:

```json
{
  "quantity": 850
}
```

---

# 17. Consumption API

## GET `/api/v1/consumption`

Returns historical consumption records.

Optional filters:

```text
location_id
category_id
start_date
end_date
```

Example:

```text
/api/v1/consumption?location_id=loc-001
```

---

## POST `/api/v1/consumption`

Adds a historical consumption record.

### Example Request

```json
{
  "location_id": "loc-001",
  "category_id": "food",
  "item_name": "Demo Supply",
  "consumption_date": "2026-09-01",
  "quantity_consumed": 125
}
```

---

# 18. Forecast API

## POST `/api/v1/forecasts/generate`

Generates a demand forecast.

### Example Request

```json
{
  "location_id": "loc-001",
  "category_id": "food",
  "horizon_days": 7
}
```

### Example Response

```json
{
  "success": true,
  "data": {
    "forecast_id": "forecast-001",
    "model": "prototype-model",
    "horizon_days": 7,
    "status": "completed"
  }
}
```

---

## GET `/api/v1/forecasts`

Returns stored forecasts.

Optional filters:

```text
location_id
category_id
start_date
end_date
```

---

## GET `/api/v1/forecasts/{forecast_id}`

Returns a specific forecast.

### Example Response

```json
{
  "success": true,
  "data": {
    "id": "forecast-001",
    "forecast_date": "2026-10-03",
    "predicted_quantity": 180,
    "lower_bound": 150,
    "upper_bound": 215,
    "model_name": "prototype-model",
    "model_version": "v1"
  }
}
```

---

# 19. Risk Assessment API

## POST `/api/v1/risk/analyze`

Calculates or updates a supply risk assessment.

### Example Request

```json
{
  "location_id": "loc-001",
  "category_id": "food"
}
```

### Example Response

```json
{
  "success": true,
  "data": {
    "risk_id": "risk-001",
    "risk_level": "medium",
    "risk_score": 0.58
  }
}
```

Risk scores shown in examples are illustrative only.

---

## GET `/api/v1/risk`

Returns risk assessments.

Optional filters:

```text
location_id
category_id
risk_level
```

---

## GET `/api/v1/risk/{risk_id}`

Returns a specific risk assessment.

---

# 20. Requirements API

## GET `/api/v1/requirements`

Returns supply requirements.

Optional filters:

```text
location_id
priority
status
required_by
```

---

## POST `/api/v1/requirements`

Creates a requirement.

### Example Request

```json
{
  "location_id": "loc-001",
  "category_id": "food",
  "required_quantity": 500,
  "priority": 2,
  "required_by": "2026-10-05T12:00:00"
}
```

---

## PATCH `/api/v1/requirements/{requirement_id}`

Updates a requirement.

---

# 21. Vehicle API

## GET `/api/v1/vehicles`

Returns available prototype vehicles.

### Example Response

```json
{
  "success": true,
  "data": [
    {
      "id": "vehicle-001",
      "vehicle_code": "DEMO-V01",
      "vehicle_type": "transport",
      "capacity": 1000,
      "unit": "units",
      "availability_status": "available"
    }
  ]
}
```

Only synthetic vehicle identifiers should be used in public demonstration data.

---

# 22. Route Optimization API

## POST `/api/v1/routes/optimize`

Requests route optimization.

### Example Request

```json
{
  "planning_date": "2026-10-05",
  "requirement_ids": [
    "req-001",
    "req-002"
  ],
  "vehicle_ids": [
    "vehicle-001",
    "vehicle-002"
  ]
}
```

### Example Response

```json
{
  "success": true,
  "data": {
    "optimization_id": "opt-001",
    "status": "completed",
    "routes_generated": 2
  }
}
```

The optimization engine may use OR-Tools or another suitable optimization library.

---

# 23. Route API

## GET `/api/v1/routes`

Returns generated routes.

Optional filters:

```text
route_date
vehicle_id
status
```

---

## GET `/api/v1/routes/{route_id}`

Returns route information.

### Example Response

```json
{
  "success": true,
  "data": {
    "id": "route-001",
    "vehicle_id": "vehicle-001",
    "total_distance": 120.5,
    "estimated_duration": 180,
    "total_load": 850,
    "status": "planned"
  }
}
```

Values are illustrative.

---

# 24. Delivery Planning API

## POST `/api/v1/delivery-plans`

Creates a delivery planning record.

### Example Request

```json
{
  "planning_date": "2026-10-05",
  "requirement_ids": [
    "req-001",
    "req-002"
  ]
}
```

---

## GET `/api/v1/delivery-plans`

Returns delivery plans.

---

## GET `/api/v1/delivery-plans/{plan_id}`

Returns a specific delivery plan.

---

# 25. Delivery API

## GET `/api/v1/deliveries`

Returns delivery records.

Optional filters:

```text
delivery_plan_id
route_id
status
```

---

## PATCH `/api/v1/deliveries/{delivery_id}`

Updates delivery status.

Example:

```json
{
  "status": "completed"
}
```

The final set of permitted statuses should be defined by the implemented business logic.

---

# 26. Scenario Simulation API

## POST `/api/v1/scenarios`

Creates a what-if scenario.

### Example Request

```json
{
  "name": "Demo Demand Increase",
  "description": "Illustrative demand change scenario"
}
```

---

## POST `/api/v1/scenarios/{scenario_id}/run`

Runs a scenario simulation.

### Example Response

```json
{
  "success": true,
  "data": {
    "scenario_id": "scenario-001",
    "status": "completed"
  }
}
```

---

## GET `/api/v1/scenarios`

Returns available scenarios.

---

## GET `/api/v1/scenarios/{scenario_id}`

Returns scenario details.

---

# 27. Scenario Results API

## GET `/api/v1/scenarios/{scenario_id}/results`

Returns simulation results.

### Example Response

```json
{
  "success": true,
  "data": {
    "baseline": {
      "routes": 5,
      "distance": 420
    },
    "scenario": {
      "routes": 6,
      "distance": 465
    }
  }
}
```

The values are illustrative.

---

# 28. Audit API

## GET `/api/v1/audit-logs`

Returns authorized audit information.

Access should be restricted according to the application's role and security model.

Optional filters:

```text
user_id
action
entity_type
start_date
end_date
```

---

# 29. Health Check API

## GET `/health`

Checks whether the API service is running.

### Example Response

```json
{
  "status": "healthy"
}
```

---

# 30. Database Health Check

## GET `/health/database`

Checks connectivity to the database.

### Example Response

```json
{
  "status": "healthy",
  "database": "connected"
}
```

The exact endpoint may be restricted or omitted in hardened deployments.

---

# 31. Service Health

A broader health endpoint can provide service status.

Example:

```text
GET /health/services
```

Possible response:

```json
{
  "api": "healthy",
  "database": "healthy",
  "forecast_service": "healthy",
  "optimization_service": "healthy"
}
```

These values are illustrative.

---

# 32. Pagination

Large API responses should support pagination.

Example:

```text
GET /api/v1/inventory?page=1&limit=20
```

Possible response:

```json
{
  "success": true,
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 120,
    "pages": 6
  }
}
```

---

# 33. Filtering and Sorting

APIs should support controlled filtering where useful.

Example:

```text
/api/v1/requirements?priority=1
```

Sorting example:

```text
/api/v1/requirements?sort=required_by
```

The final API should validate accepted filter and sorting parameters.

---

# 34. Input Validation

FastAPI/Pydantic-style validation can be used to validate requests.

Example validation rules:

```text
Quantity >= 0
Capacity > 0
Priority within allowed range
Valid UUID format
Valid date/time
Valid latitude/longitude
Required fields present
Enum values valid
```

Invalid requests should return an appropriate validation response.

---

# 35. Error Handling

The API should return consistent errors.

Example:

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Requested resource was not found"
  }
}
```

Common application error codes:

```text
VALIDATION_ERROR
UNAUTHORIZED
FORBIDDEN
RESOURCE_NOT_FOUND
CONFLICT
OPTIMIZATION_FAILED
FORECAST_FAILED
DATABASE_ERROR
INTERNAL_ERROR
```

The actual error catalog should match the implementation.

---

# 36. Optimization Failure Handling

Route optimization may fail to produce a feasible result.

Possible API response:

```json
{
  "success": false,
  "error": {
    "code": "OPTIMIZATION_FAILED",
    "message": "No feasible solution found for the supplied constraints"
  }
}
```

The frontend should present the issue clearly and allow an authorized user to review the inputs.

The system should not silently generate an invalid plan.

---

# 37. Forecast Failure Handling

If a forecast cannot be generated:

```json
{
  "success": false,
  "error": {
    "code": "FORECAST_FAILED",
    "message": "Forecast generation could not be completed"
  }
}
```

Possible causes include:

* Insufficient historical data
* Invalid input data
* Model execution failure
* Service unavailability

The final implementation should provide appropriate diagnostics without exposing sensitive information.

---

# 38. API Security

The API should follow secure development practices.

Recommended controls include:

* HTTPS in deployed environments
* Authentication
* Role-based authorization
* Input validation
* Rate limiting where appropriate
* Secure headers
* Parameterized database queries
* Secrets stored outside source code
* Audit logging
* Restricted administrative endpoints
* Controlled CORS configuration

---

# 39. CORS Configuration

The backend should only allow trusted frontend origins.

Development may use a local origin such as:

```text
http://localhost:3000
```

Production origins should be explicitly configured.

Avoid using unrestricted CORS configuration in a production deployment.

---

# 40. Secrets Management

API keys, database passwords and authentication secrets must never be hard-coded.

Example:

```text
DATABASE_URL=<secret>
SECRET_KEY=<secret>
API_KEY=<secret>
```

These values should be supplied through environment-specific secret management.

The repository should contain only safe placeholders.

---

# 41. Logging

The API should maintain structured application logs.

Useful information may include:

```text
Timestamp
Request ID
Endpoint
HTTP method
Response status
Execution time
Error code
```

Logs must not contain passwords, access tokens or other sensitive information.

---

# 42. Request Tracing

A request identifier can help trace API operations.

Example:

```text
X-Request-ID: demo-request-001
```

A request ID can connect:

```text
Frontend Request
      ↓
FastAPI
      ↓
Database / ML / Optimization
      ↓
API Response
```

This is useful for debugging and monitoring.

---

# 43. API and AI/ML Integration

The forecasting API acts as a bridge between the frontend and the ML pipeline.

```text
Frontend
   │
   ▼
POST /forecasts/generate
   │
   ▼
FastAPI
   │
   ▼
Feature Preparation
   │
   ▼
Forecast Model
   │
   ▼
Forecast Result
   │
   ▼
Database
   │
   ▼
Frontend
```

---

# 44. API and Optimization Integration

Route optimization follows a similar flow.

```text
Frontend
   │
   ▼
POST /routes/optimize
   │
   ▼
FastAPI
   │
   ▼
Requirement Validation
   │
   ▼
Optimization Engine
   │
   ▼
Optimized Routes
   │
   ▼
Database
   │
   ▼
Dashboard
```

---

# 45. API and Database Integration

The backend should act as the controlled interface to the database.

```text
React
  │
  ▼
FastAPI
  │
  ├── Authentication
  ├── Validation
  ├── Business Logic
  │
  ▼
Database Layer
  │
  ▼
PostgreSQL / PostGIS
```

The frontend should not directly connect to PostgreSQL.

---

# 46. API Testing

The API should be tested at multiple levels.

### Unit Tests

Test individual functions.

### Integration Tests

Test:

```text
API → Service → Database
```

### API Tests

Test:

* Request validation
* Authentication
* Authorization
* Response formats
* Error handling

### ML Integration Tests

Test:

```text
API → Forecast Service
```

### Optimization Tests

Test:

```text
API → Optimization Service
```

---

# 47. Example API Test

Illustrative request:

```text
POST /api/v1/forecasts/generate
```

Request:

```json
{
  "location_id": "loc-001",
  "category_id": "food",
  "horizon_days": 7
}
```

Expected result:

```text
HTTP 200
```

with a valid forecast response.

---

# 48. API Performance

Potential performance improvements include:

* Database connection pooling
* Pagination
* Caching
* Async processing for long-running jobs
* Background tasks
* Batch operations
* Efficient database queries
* Model inference optimization

Long-running forecasting or optimization operations may be executed asynchronously in a future production implementation.

---

# 49. Asynchronous Processing

A future implementation may use:

```text
API Request
     │
     ▼
Create Job
     │
     ▼
Background Worker
     │
     ├── Forecast
     └── Optimization
     │
     ▼
Store Result
     │
     ▼
Frontend Poll / Notification
```

This avoids blocking API requests for computationally expensive operations.

---

# 50. API Documentation Workflow

Developers can use the FastAPI-generated documentation during development.

```text
Start Backend
     ↓
Open API Documentation
     ↓
Inspect Endpoint
     ↓
Test Request
     ↓
Check Response
     ↓
Validate Database Result
```

---

# 51. Example End-to-End API Workflow

A complete prototype workflow can look like:

```text
1. Login
      ↓
2. Load Dashboard
      ↓
3. Retrieve Inventory
      ↓
4. Retrieve Consumption
      ↓
5. Generate Forecast
      ↓
6. Calculate Risk
      ↓
7. Create Requirements
      ↓
8. Optimize Routes
      ↓
9. Create Delivery Plan
      ↓
10. Run What-If Scenario
      ↓
11. Review Results
      ↓
12. Record Final Planning Action
```

---

# 52. API Project Structure

A possible FastAPI project structure is:

```text
src/
├── api/
│   ├── main.py
│   ├── dependencies.py
│   │
│   └── routes/
│       ├── auth.py
│       ├── dashboard.py
│       ├── locations.py
│       ├── inventory.py
│       ├── consumption.py
│       ├── forecasts.py
│       ├── risk.py
│       ├── requirements.py
│       ├── vehicles.py
│       ├── routes.py
│       ├── deliveries.py
│       ├── scenarios.py
│       └── audit.py
│
├── database/
├── ml/
├── optimization/
└── services/
```

The actual project structure should reflect the implemented codebase.

---

# 53. Responsible API Design

The API is intended to support decision-making rather than replace human judgment.

The intended architecture is:

```text
Data
 ↓
AI / Optimization
 ↓
Recommendation
 ↓
Human Review
 ↓
Planning Decision
```

AI-generated forecasts and optimization outputs should be treated as decision-support information.

---

# 54. Data Responsibility

The public API documentation and prototype should use:

* Synthetic data
* Artificial identifiers
* Non-sensitive demonstration locations
* Simulated inventory
* Simulated consumption
* Demonstration vehicles
* Artificial scenarios

The project must not expose:

* Classified information
* Restricted military information
* Sensitive operational routes
* Real operational schedules
* Sensitive personnel information
* Authentication credentials
* Private API keys

---

# 55. Current Prototype Status

| API Component             | Status               |
| ------------------------- | -------------------- |
| FastAPI architecture      | Proposed / Prototype |
| Authentication API        | Proposed             |
| Dashboard API             | Proposed             |
| Inventory API             | Proposed             |
| Consumption API           | Proposed             |
| Forecast API              | Proposed             |
| Risk API                  | Proposed             |
| Requirements API          | Proposed             |
| Vehicle API               | Proposed             |
| Route Optimization API    | Proposed             |
| Delivery API              | Proposed             |
| Scenario API              | Proposed             |
| Audit API                 | Proposed             |
| Production authentication | Future               |
| Production monitoring     | Future               |

Update this table as endpoints are implemented.

---

# 56. Future API Enhancements

Potential future improvements include:

* WebSocket updates
* Background job queues
* Advanced authentication
* Fine-grained permissions
* API rate limiting
* Advanced monitoring
* Model management APIs
* Forecast comparison APIs
* Optimization job tracking
* Notification APIs
* Automated data-quality APIs
* Versioned ML model endpoints

---

# 57. Summary

The RASAD-AI API provides a modular interface between the frontend, database, AI/ML services and route optimization engine.

The primary flow is:

```text
React Dashboard
       ↓
FastAPI
       ↓
Authentication + Validation
       ↓
Business Services
       ↓
PostgreSQL / PostGIS
       ↓
AI/ML + Optimization
       ↓
Planning Results
       ↓
Dashboard
```

The API design supports:

* Inventory management
* Demand forecasting
* Risk assessment
* Requirement management
* Route optimization
* Delivery planning
* What-if simulation
* Dashboard reporting
* Auditability

The API should remain secure, versioned, validated and human-supervised.

> **Responsible-use note:** This documentation describes a prototype decision-support architecture using synthetic or authorized non-sensitive data. It must not be used to expose or process classified, restricted or operationally sensitive information.

---

## Document Status

**Project:** RASAD-AI
**Problem Statement:** SIH26251
**Document:** API Documentation
**Status:** Prototype / Proposed Architecture
**Backend:** FastAPI
**Database:** PostgreSQL + PostGIS
**Data Classification:** Synthetic / Non-Sensitive Demonstration Data
**Last Updated:** 2026
