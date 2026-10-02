# 🚀 RASAD-AI — Deployment Documentation

## 1. Overview

RASAD-AI is a predictive logistics decision-support prototype designed to combine:

* Demand forecasting
* Inventory analysis
* Stock-out risk assessment
* Requirement prioritization
* Route optimization
* What-if simulation
* Command dashboard
* API-based backend services

This document explains how the project can be configured, run, tested, containerized, and prepared for deployment.

The current repository is intended primarily for **development, academic demonstration, SIH evaluation, and prototype testing**.

> **Important:** The public repository must use synthetic, public, or appropriately authorized non-sensitive data. Classified, restricted, confidential, or operationally sensitive information must not be included.

---

# 2. Deployment Architecture

The intended deployment architecture is:

```text
                    ┌──────────────────────┐
                    │      User / Admin    │
                    └──────────┬───────────┘
                               |
                               v
                    ┌──────────────────────┐
                    │   React Dashboard    │
                    │   + Leaflet Maps     │
                    └──────────┬───────────┘
                               |
                               | HTTPS / REST API
                               v
                    ┌──────────────────────┐
                    │     FastAPI Backend  │
                    └──────────┬───────────┘
                               |
             ┌─────────────────┼──────────────────┐
             |                 |                  |
             v                 v                  v
      ┌─────────────┐  ┌──────────────┐  ┌──────────────┐
      │ AI/ML Engine│  │ Risk Engine  │  │ OR-Tools     │
      │ Forecasting │  │              │  │ Optimizer    │
      └─────────────┘  └──────────────┘  └──────────────┘
             |                 |                  |
             └─────────────────┼──────────────────┘
                               v
                    ┌──────────────────────┐
                    │ PostgreSQL + PostGIS │
                    └──────────────────────┘
```

---

# 3. Deployment Environments

RASAD-AI can conceptually be deployed in multiple environments.

## 3.1 Local Development

Used by developers for:

* Coding
* Debugging
* Unit testing
* API testing
* UI development
* Model experimentation

Typical components:

```text
Developer Machine
├── Backend
├── Frontend
├── PostgreSQL
└── Synthetic Dataset
```

---

## 3.2 Docker Development

Docker can be used to provide consistent development environments.

Example architecture:

```text
Docker Environment
├── Backend Container
├── Frontend Container
└── PostgreSQL Container
```

Additional services can be added when required.

---

## 3.3 Demonstration Environment

A demonstration environment can run the complete prototype using synthetic data.

Example:

```text
Browser
   |
   v
React Dashboard
   |
   v
FastAPI
   |
   ├── Forecasting
   ├── Risk Analysis
   └── Route Optimization
   |
   v
PostgreSQL
```

---

## 3.4 Production-Style Environment

A production-style deployment may include:

```text
Internet / Controlled Network
            |
            v
       Reverse Proxy
            |
            v
       FastAPI Backend
            |
      ┌─────┴─────┐
      |           |
      v           v
 PostgreSQL    AI/ML Services
      |
      v
 Backup / Monitoring
```

Actual production deployment requirements depend on the organization's infrastructure and security policies.

---

# 4. System Requirements

The exact requirements depend on the implementation size and workload.

Recommended development environment:

| Component         | Recommended                           |
| ----------------- | ------------------------------------- |
| OS                | Linux / Windows / macOS               |
| Python            | 3.11                                  |
| Node.js           | Current LTS                           |
| Database          | PostgreSQL                            |
| Spatial Extension | PostGIS                               |
| Containerization  | Docker                                |
| API Framework     | FastAPI                               |
| Frontend          | React                                 |
| Browser           | Modern Chromium/Firefox-based browser |
| RAM               | 8 GB or more recommended              |
| Storage           | 10 GB+ available space                |

For larger AI/ML workloads, additional CPU, RAM, or GPU resources may be useful.

---

# 5. Repository Structure

The intended project structure is:

```text
army-predictive-logistics-sih/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── assets/
│
├── data/
│
├── docs/
│   ├── problem-statement.md
│   ├── solution-architecture.md
│   ├── system-workflow.md
│   ├── ai-ml-model.md
│   ├── route-optimization.md
│   ├── database-design.md
│   ├── api-documentation.md
│   ├── testing-strategy.md
│   ├── security.md
│   └── deployment.md
│
├── src/
│
└── dashboard/
```

The exact implementation structure may evolve during development.

---

# 6. Clone the Repository

Clone the repository using the project's actual GitHub URL.

Example:

```bash
git clone https://github.com/amrut4469-blip/army-predictive-logistics-sih.git
```

Move into the project:

```bash
cd army-predictive-logistics-sih
```

Verify the repository:

```bash
git status
```

---

# 7. Python Environment

Create a Python virtual environment.

Linux/macOS:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, verify:

```bash
python --version
```

---

# 8. Install Python Dependencies

If the repository contains `requirements.txt`, install dependencies using:

```bash
pip install -r requirements.txt
```

Verify installed packages:

```bash
pip list
```

The exact dependency list should match the project's actual implementation.

---

# 9. PostgreSQL Setup

RASAD-AI is designed to use PostgreSQL for structured application data.

A development database can be created using PostgreSQL tools.

Example:

```sql
CREATE DATABASE rasad_ai;
```

The database should be accessible only to authorized development services.

---

# 10. PostGIS Setup

If geographic features are implemented, PostGIS can be enabled.

Example:

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
```

PostGIS can support geographic data such as:

* Locations
* Distances
* Geographic relationships
* Route-related information

The public prototype should use synthetic or non-sensitive geographic data.

---

# 11. Environment Variables

Application configuration should be stored outside source code.

Create a local `.env` file if the implementation uses environment variables.

Example:

```env
APP_ENV=development
DEBUG=true

DATABASE_URL=postgresql://username:password@localhost:5432/rasad_ai

SECRET_KEY=replace_with_local_secret

API_HOST=127.0.0.1
API_PORT=8000
```

These values are examples only.

Never commit real credentials to GitHub.

---

# 12. `.env.example`

The repository may provide:

```text
.env.example
```

Example:

```env
APP_ENV=
DEBUG=

DATABASE_URL=

SECRET_KEY=

API_HOST=
API_PORT=
```

Only variable names and safe placeholders should be included.

---

# 13. Backend Startup

The FastAPI backend can be started using the project's actual application entry point.

A common FastAPI structure may use:

```bash
uvicorn src.main:app --reload
```

If the project uses a different module path, the command should be adjusted to match the implementation.

Typical development server:

```text
http://127.0.0.1:8000
```

---

# 14. API Documentation

FastAPI can automatically expose API documentation.

Typical development endpoints include:

```text
/docs
```

and:

```text
/redoc
```

These should be protected or disabled appropriately in controlled production environments if required by the deployment policy.

---

# 15. Backend Health Check

A health endpoint can be used to verify whether the backend is running.

Example:

```text
GET /health
```

Expected conceptual response:

```json
{
  "status": "ok"
}
```

A production health check may also verify dependencies such as the database.

---

# 16. Frontend Setup

If the dashboard uses React, install the frontend dependencies.

From the dashboard directory:

```bash
cd dashboard
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

or, depending on the project configuration:

```bash
npm start
```

The actual command should match the frontend framework and package configuration used by the repository.

---

# 17. Frontend API Configuration

The frontend should communicate with the backend through a configurable API base URL.

Example development configuration:

```text
API_BASE_URL=http://127.0.0.1:8000
```

Production configuration should point to the approved backend service.

API endpoints should not be hard-coded throughout the frontend application.

---

# 18. Database Initialization

Before running database-dependent functionality:

1. Start PostgreSQL.
2. Create the application database.
3. Enable required extensions.
4. Apply database schema or migrations.
5. Insert approved synthetic/demo data.
6. Verify database connectivity.

Conceptual workflow:

```text
PostgreSQL
    |
    v
Create Database
    |
    v
Create Schema
    |
    v
Run Migrations
    |
    v
Load Synthetic Data
    |
    v
Verify Connection
```

---

# 19. Database Migrations

If the project uses a migration framework, schema changes should be applied through migrations rather than manually modifying production databases.

A migration workflow may look like:

```text
Code Change
    |
    v
Migration File
    |
    v
Review
    |
    v
Test Database
    |
    v
Apply Migration
```

The exact migration commands depend on the framework used by the implementation.

---

# 20. Loading Synthetic Data

The demonstration environment should use synthetic data.

Example data categories:

```text
data/
├── inventory.csv
├── consumption.csv
├── locations.csv
├── vehicles.csv
└── requirements.csv
```

These filenames are illustrative and should only be created if the corresponding datasets exist in the implementation.

Data should be validated before loading.

---

# 21. Data Validation Before Deployment

Before starting the complete system, verify:

* Required columns exist
* Numeric fields contain valid values
* Dates are correctly formatted
* Missing values are handled
* Duplicate records are controlled
* Location data is valid
* Inventory quantities are valid
* Vehicle capacities are valid
* No protected information is included

---

# 22. Running the Complete System Locally

A typical local workflow is:

### Terminal 1 — Database

Start PostgreSQL.

### Terminal 2 — Backend

```bash
source .venv/bin/activate
uvicorn src.main:app --reload
```

### Terminal 3 — Frontend

```bash
cd dashboard
npm install
npm run dev
```

Then open the frontend development address displayed by the frontend tooling.

---

# 23. Local System Flow

```text
Developer Browser
       |
       v
React Dashboard
       |
       | API
       v
FastAPI
       |
       ├── Forecasting
       ├── Risk Engine
       ├── Requirement Prioritization
       └── Route Optimization
       |
       v
PostgreSQL + PostGIS
```

---

# 24. Docker Deployment

Docker can be used to package the application components.

A conceptual Docker architecture is:

```text
Docker Compose
│
├── frontend
│
├── backend
│
└── postgres
```

Additional services can be introduced if required by the final implementation.

---

# 25. Example Docker Workflow

If a valid `Dockerfile` is present:

```bash
docker build -t rasad-ai-backend .
```

Run the container:

```bash
docker run --rm -p 8000:8000 rasad-ai-backend
```

The exact Docker commands depend on the project's final Docker configuration.

---

# 26. Docker Compose

If the project contains a `docker-compose.yml` or `compose.yaml`, the complete stack may be started using:

```bash
docker compose up --build
```

To stop the stack:

```bash
docker compose down
```

To run in detached mode:

```bash
docker compose up -d --build
```

These commands should only be used after the corresponding Docker configuration has been added to the project.

---

# 27. Production Configuration

Production deployments should use separate configuration from development.

Important differences include:

| Development               | Production               |
| ------------------------- | ------------------------ |
| Debug enabled when needed | Debug disabled           |
| Local database            | Protected database       |
| Development credentials   | Managed secrets          |
| Local HTTP                | HTTPS/TLS                |
| Detailed logs             | Controlled logs          |
| Development CORS          | Restricted CORS          |
| Hot reload                | Disabled                 |
| Test data                 | Approved deployment data |

---

# 28. Reverse Proxy

A production-style deployment may use a reverse proxy.

Conceptually:

```text
Client
  |
  v
HTTPS
  |
  v
Reverse Proxy
  |
  +----------------+
  |                |
  v                v
Frontend         FastAPI
                    |
                    v
                PostgreSQL
```

The reverse proxy can provide:

* TLS termination
* Request routing
* Security headers
* Connection management
* Static content delivery

The exact implementation depends on the deployment environment.

---

# 29. HTTPS

Production communication should use HTTPS.

TLS certificates should be managed according to the deployment environment.

The application should not expose sensitive authenticated traffic over plain HTTP in production.

---

# 30. Secure Deployment Configuration

Before production-style deployment:

* Disable debug mode.
* Remove development credentials.
* Configure secure secrets.
* Restrict database access.
* Configure allowed frontend origins.
* Enable HTTPS.
* Review exposed ports.
* Review API documentation exposure.
* Enable appropriate logging.
* Verify backup configuration.

---

# 31. Database Connectivity Check

The backend should verify database connectivity during deployment validation.

Conceptual health flow:

```text
Backend
   |
   v
Database Connection
   |
   +---- Success ---> Service Ready
   |
   +---- Failure ---> Service Not Ready
```

The application should fail clearly rather than silently continuing with an unavailable database.

---

# 32. AI/ML Model Deployment

If forecasting models are implemented, model artifacts should be version controlled appropriately.

A model deployment workflow may be:

```text
Training Data
     |
     v
Training
     |
     v
Evaluation
     |
     v
Approved Model
     |
     v
Model Registry / Artifact Storage
     |
     v
Inference Service
```

Only validated model versions should be used for demonstrations.

---

# 33. Route Optimization Deployment

The route optimization component should run only after required inputs have been validated.

Typical flow:

```text
Requirements
     |
     v
Inventory / Supply Data
     |
     v
Vehicle Constraints
     |
     v
Optimization Engine
     |
     v
Feasible Route Plan
```

If no feasible solution exists, the system should return a controlled error and request review of the inputs or constraints.

---

# 34. Offline / Controlled Deployment

The architecture may support controlled or offline-capable environments depending on implementation.

A conceptual controlled environment is:

```text
┌─────────────────────────────────────┐
│       Controlled Network            │
│                                     │
│  ┌──────────┐     ┌─────────────┐  │
│  │ Frontend │ --> │ FastAPI     │  │
│  └──────────┘     └──────┬──────┘  │
│                          |         │
│                   ┌──────v──────┐  │
│                   │ PostgreSQL  │  │
│                   └─────────────┘  │
│                                     │
└─────────────────────────────────────┘
```

The exact offline behavior depends on which external services the final implementation requires.

---

# 35. Deployment Health Checks

Before declaring the system ready, verify:

### Application

* Backend starts successfully.
* Frontend loads successfully.
* API endpoints respond.

### Database

* Database connection works.
* Required tables exist.
* Required extensions are available.

### AI/ML

* Model artifacts load successfully.
* Forecast requests return valid results.

### Optimization

* Valid scenarios produce results.
* Invalid scenarios fail safely.

### Security

* Secrets are not exposed.
* Debug mode is disabled where required.
* Authentication and authorization work.

---

# 36. Smoke Testing

A deployment smoke test should verify the most important user workflow.

Example:

```text
Login
  |
  v
Dashboard
  |
  v
Select Supply Category
  |
  v
View Forecast
  |
  v
View Risk
  |
  v
Generate Delivery Plan
  |
  v
Review Result
```

The exact workflow depends on the implemented frontend.

---

# 37. Troubleshooting

## Backend does not start

Check:

```bash
python --version
```

Verify dependencies:

```bash
pip install -r requirements.txt
```

Check environment variables.

Check the backend module path.

---

## Database connection fails

Verify:

* PostgreSQL is running.
* Database exists.
* Username is correct.
* Password is correct.
* Port is correct.
* `DATABASE_URL` is correct.
* Network access is available.

---

## Frontend does not start

Verify:

```bash
node --version
npm --version
```

Then:

```bash
npm install
```

Check frontend environment variables and API configuration.

---

## API requests fail

Check:

1. Backend is running.
2. Correct API base URL is configured.
3. CORS configuration is correct.
4. Authentication credentials are valid.
5. Request payload matches the API schema.

---

## Forecasting fails

Check:

* Input dataset
* Date fields
* Missing values
* Model artifact
* Feature availability
* Required model dependencies

The system should return a controlled error rather than an unexplained failure.

---

## Route optimization fails

Check:

* Locations
* Requirements
* Vehicle capacity
* Constraint configuration
* Missing data
* Feasibility

An infeasible optimization problem should be reported explicitly.

---

# 38. Deployment Logging

Deployment logs should capture useful technical information such as:

* Service startup
* Service shutdown
* Database connectivity
* API errors
* Model loading
* Optimization errors
* Health-check status

Logs should never expose:

* Passwords
* API keys
* Authentication tokens
* Secret configuration
* Protected information

---

# 39. Monitoring

A production-style deployment may monitor:

* API availability
* Response time
* Error rate
* Database availability
* CPU usage
* Memory usage
* Storage usage
* Model failures
* Optimization failures

Monitoring should focus on system reliability without collecting unnecessary sensitive information.

---

# 40. Backup and Recovery

Database backups should be configured according to the deployment environment.

A basic process is:

```text
Production Database
        |
        v
     Backup
        |
        v
Protected Storage
        |
        v
Recovery Test
```

Backups should be access-controlled and protected appropriately.

---

# 41. Updating the Application

A controlled update workflow should be used.

```text
New Code
   |
   v
Tests
   |
   v
Security Review
   |
   v
Build
   |
   v
Deployment
   |
   v
Health Check
   |
   v
Monitoring
```

Production updates should not be performed without appropriate testing.

---

# 42. Rollback

If an update causes a critical failure, the deployment process should support rollback where practical.

Possible rollback components include:

* Application version
* Frontend build
* Database migration
* Model version
* Configuration

Rollback procedures should be tested before relying on them in a production environment.

---

# 43. CI/CD

Future versions may include automated CI/CD.

A conceptual pipeline:

```text
Git Push
   |
   v
Lint
   |
   v
Unit Tests
   |
   v
Integration Tests
   |
   v
Security Checks
   |
   v
Build
   |
   v
Deployment
```

The repository can use GitHub Actions or another approved CI/CD platform.

---

# 44. Deployment Security Checklist

Before deployment:

* [ ] Production configuration is separate from development configuration.
* [ ] Debug mode is disabled where required.
* [ ] No secrets are stored in source code.
* [ ] `.env` files are not committed.
* [ ] Database credentials are protected.
* [ ] HTTPS is configured.
* [ ] CORS is restricted appropriately.
* [ ] Authentication is enabled where required.
* [ ] Authorization is tested.
* [ ] API inputs are validated.
* [ ] Dependencies are reviewed.
* [ ] Database access is restricted.
* [ ] Logs do not expose secrets.
* [ ] Backups are configured.
* [ ] Health checks are working.
* [ ] Synthetic/authorized non-sensitive data is being used.
* [ ] No classified or restricted information is included.

---

# 45. SIH Demonstration Deployment

For an SIH demonstration, the recommended prototype workflow is:

```text
Laptop / Demo Machine
        |
        v
Frontend Dashboard
        |
        v
FastAPI Backend
        |
        ├── Forecasting
        ├── Risk Analysis
        ├── Requirement Prioritization
        └── Route Optimization
        |
        v
PostgreSQL
        |
        v
Synthetic Dataset
```

The demonstration should focus on showing:

1. Data ingestion
2. Demand prediction
3. Risk identification
4. Requirement prioritization
5. Route optimization
6. What-if scenario analysis
7. Dashboard visualization
8. Human review of recommendations

---

# 46. Demo Data Policy

The SIH demonstration should use:

* Synthetic inventory data
* Synthetic consumption data
* Synthetic vehicle information
* Synthetic requirements
* Demonstration locations
* Simulated disruptions
* Artificial forecast results where required

No real protected logistics information should be used for the public demonstration.

---

# 47. Deployment Acceptance Criteria

A deployment can be considered ready for prototype demonstration when:

### Application

* Frontend starts successfully.
* Backend starts successfully.
* Database is accessible.

### Functionality

* Dashboard loads.
* Data can be retrieved.
* Forecasting workflow works.
* Risk workflow works.
* Optimization workflow works.
* Scenario workflow works.

### Reliability

* Invalid inputs fail safely.
* Database failures are handled.
* Optimization infeasibility is reported.
* API errors are controlled.

### Security

* Secrets are protected.
* Debug configuration is reviewed.
* Access controls are tested.
* Repository contains no protected information.

---

# 48. Current Prototype Deployment Status

The deployment documentation describes the intended deployment architecture and procedures.

The exact commands and services should always match the actual implementation present in the repository.

Features may exist at different stages:

### Designed

* FastAPI backend
* React dashboard
* PostgreSQL/PostGIS
* AI/ML pipeline
* Route optimization
* Docker-based deployment concept
* Secure configuration

### Prototype / Development

Some deployment components may still require implementation or integration, including:

* Final Docker configuration
* Production authentication
* Production reverse proxy
* Production TLS
* CI/CD pipeline
* Centralized monitoring
* Automated deployment

Documentation should not be treated as proof that a feature has already been implemented.

---

# 49. Future Deployment Enhancements

Future versions may include:

* Docker Compose production configuration
* Kubernetes deployment
* Automated CI/CD
* Cloud deployment
* On-premise deployment package
* Health monitoring
* Centralized logging
* Automated backups
* Model registry
* Container scanning
* Infrastructure-as-code
* Automated rollback
* High-availability architecture

The selected deployment architecture should depend on the requirements of the actual deployment environment.

---

# 50. Deployment Best Practices

The following principles should be maintained:

1. Keep development and production configurations separate.
2. Never commit secrets.
3. Validate configuration before startup.
4. Keep dependencies updated.
5. Use HTTPS for production communication.
6. Restrict database access.
7. Monitor application health.
8. Maintain backups.
9. Test recovery procedures.
10. Keep human oversight for important recommendations.
11. Use synthetic or authorized non-sensitive data for demonstrations.
12. Document implemented features separately from planned features.

---

# 51. Final Deployment Workflow

The complete deployment workflow can be summarized as:

```text
                 ┌────────────────────┐
                 │   Source Code      │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Dependency Setup   │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Database Setup     │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Environment Config │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Backend Startup    │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Frontend Startup   │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Integration Tests  │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Security Checks    │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Health Checks      │
                 └─────────┬──────────┘
                           |
                           v
                 ┌────────────────────┐
                 │ Demonstration /    │
                 │ Controlled Deploy  │
                 └────────────────────┘
```

---

# 52. Conclusion

RASAD-AI is structured to support a modular deployment architecture consisting of:

* React dashboard
* FastAPI backend
* AI/ML services
* Risk analysis
* Route optimization
* PostgreSQL/PostGIS
* Synthetic demonstration data

The deployment process should prioritize:

* Reproducibility
* Security
* Reliability
* Maintainability
* Testability
* Controlled configuration
* Human oversight

The current repository is primarily an SIH prototype and academic demonstration. Any future real-world deployment would require additional validation, security review, infrastructure approval, data governance, and organization-specific controls.

---

## Responsible Deployment Notice

RASAD-AI should be demonstrated using synthetic, public, or appropriately authorized non-sensitive data.

This documentation describes a software deployment architecture and does not provide operational military deployment procedures.

No classified, restricted, confidential, or operationally sensitive information should be included in the public repository or demonstration environment.
