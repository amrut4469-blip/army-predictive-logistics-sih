# 🚚 RASAD-AI — Route Optimization

## 1. Overview

The Route Optimization module is responsible for generating candidate delivery plans while considering defined planning constraints.

The module connects predicted requirements with available delivery resources and attempts to produce a feasible and efficient routing solution.

The conceptual workflow is:

```text
Forecasted Requirements
        ↓
Risk / Priority Analysis
        ↓
Delivery Requirements
        ↓
Vehicle Availability
        ↓
Vehicle Capacity
        ↓
Route Constraints
        ↓
Optimization Solver
        ↓
Candidate Delivery Plan
        ↓
Constraint Validation
        ↓
Human Review
```

The optimization output is intended as decision-support information and should remain subject to authorized human review.

---

# 2. Optimization Objectives

The module can be configured to optimize one or more planning objectives.

Potential objectives include:

* Minimize total travel distance
* Minimize travel time
* Improve vehicle utilization
* Satisfy delivery requirements
* Reduce unnecessary trips
* Respect vehicle capacity
* Respect route constraints
* Prioritize higher-risk requirements

The exact objective function depends on the final implementation and available data.

---

# 3. Vehicle Routing Problem

The delivery planning problem can be represented as a constrained vehicle-routing problem.

A simplified representation is:

```text
                    ┌─────────────┐
                    │ Depot /     │
                    │ Supply Point│
                    └──────┬──────┘
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
        Location A     Location B    Location C
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                    Return / End
```

The optimizer determines a feasible sequence according to the configured constraints.

---

# 4. Inputs

The optimization engine can receive the following inputs.

## 4.1 Delivery Requirements

Each requirement can contain information such as:

* Location identifier
* Supply category
* Required quantity
* Priority
* Delivery time information where applicable

---

## 4.2 Vehicle Information

Vehicle records can contain:

* Vehicle identifier
* Capacity
* Availability
* Start location
* End location
* Other configured constraints

Example:

| Vehicle | Capacity | Available |
| ------- | -------: | --------- |
| V-001   |     1000 | Yes       |
| V-002   |      750 | Yes       |
| V-003   |      500 | No        |

These are illustrative prototype values.

---

## 4.3 Location Information

The optimizer may use:

* Location identifier
* Coordinates or spatial representation
* Delivery requirement
* Accessibility status
* Other authorized planning information

---

## 4.4 Route Information

Routes may include:

* Available / unavailable status
* Estimated travel distance
* Estimated travel time
* Configured constraints

The prototype should use simulated route information.

---

# 5. Optimization Workflow

The complete workflow is:

```text
┌──────────────────────────┐
│ Forecasted Demand        │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Risk Assessment          │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Delivery Requirements    │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Vehicle Data             │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Route / Distance Data    │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Constraints              │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Optimization Solver      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Candidate Route Plan     │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Constraint Validation    │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Human Review             │
└──────────────────────────┘
```

---

# 6. OR-Tools

The project can use Google OR-Tools for vehicle-routing and mathematical optimization problems.

OR-Tools can support problems involving:

* Vehicle routing
* Capacity constraints
* Distance optimization
* Time-related constraints
* Assignment problems
* Other combinatorial optimization tasks

The exact OR-Tools configuration should correspond to the implemented optimization module.

---

# 7. Basic Vehicle Routing Model

A simplified routing model contains:

```text
Vehicles
    +
Locations
    +
Demand
    +
Distance Matrix
    +
Constraints
    ↓
Optimization Model
    ↓
Route Assignment
```

The solver attempts to find a feasible solution according to the configured objective and constraints.

---

# 8. Distance Matrix

The optimizer can use a distance matrix.

Example:

| From / To | Depot |  A |  B |  C |
| --------- | ----: | -: | -: | -: |
| Depot     |     0 | 10 | 15 | 20 |
| A         |    10 |  0 |  8 | 12 |
| B         |    15 |  8 |  0 |  7 |
| C         |    20 | 12 |  7 |  0 |

The values above are fictional and used only for demonstration.

A real implementation may calculate distances from an authorized spatial dataset.

---

# 9. Capacity Constraint

Vehicle capacity must be respected.

Example:

```text
Vehicle Capacity = 1000 units
```

If a proposed route requires:

```text
Total Load = 850 units
```

then:

```text
850 ≤ 1000
```

The route satisfies the capacity constraint.

If:

```text
Total Load = 1200 units
```

then:

```text
1200 > 1000
```

The route is infeasible for that vehicle.

---

# 10. Requirement Constraint

The system should account for delivery requirements.

Example:

```text
Location A → 300 units
Location B → 250 units
Location C → 200 units
```

Total requirement:

```text
300 + 250 + 200 = 750 units
```

A vehicle with capacity 1000 units could potentially carry the total quantity, subject to other constraints.

These are illustrative values only.

---

# 11. Priority-Aware Planning

Forecasting and risk analysis can provide priority information.

Conceptual flow:

```text
Forecast
   ↓
Inventory Coverage
   ↓
Risk
   ↓
Priority
   ↓
Optimization
```

Higher-priority requirements can be represented as optimization constraints or objective penalties, depending on the implementation.

The prioritization mechanism should remain transparent and configurable.

---

# 12. Route Constraints

The optimizer can account for route availability.

Example:

```text
Route A → Available
Route B → Unavailable
Route C → Available
```

The planning engine should exclude unavailable routes from candidate solutions where the data model supports this constraint.

All demonstration route data should remain synthetic or otherwise authorized.

---

# 13. Disruption-Aware Re-Planning

One important capability of the project is the ability to evaluate a new planning scenario when a route constraint changes.

Conceptual workflow:

```text
Existing Plan
     ↓
Route Constraint Changes
     ↓
Identify Affected Routes
     ↓
Update Optimization Inputs
     ↓
Run Solver
     ↓
Generate Alternative Plan
     ↓
Validate Constraints
     ↓
Human Review
```

The purpose is to allow rapid evaluation of alternative plans.

---

# 14. What-If Route Simulation

The what-if simulator can allow users to modify selected assumptions.

Possible simulated changes include:

### Scenario 1 — Route Unavailable

```text
Route X
   ↓
Unavailable
   ↓
Re-optimization
   ↓
Alternative Candidate Plan
```

### Scenario 2 — Vehicle Unavailable

```text
Vehicle V-002
   ↓
Unavailable
   ↓
Re-optimization
   ↓
Updated Plan
```

### Scenario 3 — Demand Increase

```text
Demand
  +20%
   ↓
Updated Requirements
   ↓
Re-optimization
   ↓
Updated Candidate Plan
```

These scenarios are simulations and do not automatically modify real-world systems.

---

# 15. Objective Function

A simplified optimization objective may be represented as:

```text
Minimize:

Total Travel Cost
+
Constraint Penalties
+
Optional Priority Penalties
```

The actual objective function depends on the implemented solver configuration.

The objective should be documented in the source code and tested with representative synthetic cases.

---

# 16. Constraint Types

The optimization module can support several constraint categories.

### Capacity

Vehicle capacity should not be exceeded.

### Availability

Only available vehicles and routes should be considered.

### Demand

Required quantities should be represented correctly.

### Assignment

Each requirement should be assigned according to the configured planning rules.

### Time

If time windows are implemented, deliveries should respect configured windows.

### Resource

Available vehicles or other planning resources should not be over-allocated.

---

# 17. Feasibility Checking

After optimization, the generated solution should be validated.

```text
Candidate Solution
       ↓
Capacity Check
       ↓
Route Check
       ↓
Demand Check
       ↓
Resource Check
       ↓
Time Check
       ↓
Feasible / Infeasible
```

If a solution is infeasible, the system should provide an understandable error or status message.

---

# 18. No-Feasible-Solution Case

An optimization problem may have no feasible solution under the current constraints.

Example:

```text
Required Demand = 5000 units
Available Capacity = 3000 units
```

The system should not falsely report a successful plan.

Instead:

```text
No Feasible Solution
        ↓
Identify Constraint
        ↓
Notify User
        ↓
Allow Parameter Review
```

The exact handling strategy depends on the implementation.

---

# 19. Route Optimization Output

The optimizer can produce structured output such as:

| Field     | Description              |
| --------- | ------------------------ |
| Vehicle   | Selected vehicle         |
| Sequence  | Delivery sequence        |
| Locations | Candidate stops          |
| Load      | Assigned quantity        |
| Distance  | Estimated route distance |
| Status    | Feasible / infeasible    |
| Objective | Optimization value       |

Example:

```text
Vehicle: V-001
Route: Depot → A → B → C
Load: 750 units
Distance: 42 km
Status: Feasible
```

The values are illustrative.

---

# 20. Dashboard Integration

The optimization results are sent to the backend and displayed through the dashboard.

```text
Optimization Engine
        ↓
Candidate Plan
        ↓
FastAPI
        ↓
React Dashboard
        ↓
Map + Tables + Metrics
        ↓
Human Review
```

The dashboard can show:

* Candidate routes
* Vehicle assignments
* Delivery sequence
* Load
* Route distance
* Constraint status

---

# 21. Map Visualization

The frontend can visualize candidate routes using a mapping library such as Leaflet.

Conceptual representation:

```text
              Location B
                  ●
                 /
                /
       Location A ●
              /
             /
        ● Depot
             \
              \
               ● Location C
```

The exact map implementation depends on the frontend module.

The public prototype should use synthetic or non-sensitive locations.

---

# 22. Optimization Performance

The optimization module can be evaluated using:

### Feasibility

Percentage of generated solutions satisfying constraints.

### Objective Value

Measured value of the configured optimization objective.

### Computation Time

Time required to generate a candidate solution.

### Resource Utilization

Vehicle capacity or other configured resource utilization.

### Re-Planning Time

Time required to generate a new candidate plan after a simulated constraint change.

Actual performance values should be measured from the implemented prototype rather than assumed.

---

# 23. Testing Strategy

The optimizer should be tested using synthetic scenarios.

### Test 1 — Basic Feasible Case

Input:

```text
1 vehicle
3 locations
Demand within vehicle capacity
All routes available
```

Expected:

```text
Feasible solution
```

### Test 2 — Capacity Violation

Input demand exceeds all available vehicle capacity.

Expected:

```text
No feasible solution
```

### Test 3 — Route Constraint

One route is marked unavailable.

Expected:

```text
Solver avoids the unavailable route
```

where the implemented model supports this constraint.

### Test 4 — Vehicle Unavailable

One vehicle is removed from the available fleet.

Expected:

```text
Updated candidate plan
```

if another feasible solution exists.

---

# 24. Integration with Forecasting

The optimization engine should not directly generate demand forecasts.

Instead:

```text
Forecasting Module
        ↓
Predicted Demand
        ↓
Risk Engine
        ↓
Priority Requirements
        ↓
Optimization Engine
```

This separation makes the architecture modular and easier to test.

---

# 25. Integration with Risk Engine

Risk information can be used to help organize planning priorities.

```text
Inventory
    +
Forecast
    ↓
Risk Engine
    ↓
Priority Information
    ↓
Optimization
```

The exact relationship between risk and optimization should be configurable.

---

# 26. Human-in-the-Loop

The optimization output is a candidate plan.

The system should clearly indicate:

```text
Generated by System
        ↓
Review Required
        ↓
Authorized User
        ↓
Approve / Modify / Reject
```

The software should not automatically execute operational actions based only on the optimization result.

---

# 27. Security Considerations

The optimization module should follow the application's overall security model.

Recommended controls include:

* Authentication
* Role-based authorization
* Input validation
* Audit logging
* Secure API communication
* Controlled deployment
* Secret management

The repository must not contain sensitive operational routes or real restricted logistics information.

---

# 28. Synthetic Data Requirement

All public demonstrations should use:

* Synthetic locations
* Synthetic route distances
* Synthetic vehicle information
* Synthetic demand
* Synthetic inventory

Example:

```text
Depot-A
Location-01
Location-02
Location-03
```

These identifiers are intentionally generic.

---

# 29. Optimization Pipeline

The complete module can be summarized as:

```text
┌───────────────────────────┐
│ Forecasted Requirements   │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Risk / Priority Engine    │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Vehicle & Resource Data   │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Route / Distance Data     │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Constraints               │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ OR-Tools / Solver         │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Candidate Route Plan      │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Feasibility Validation    │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Dashboard                 │
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│ Human Review              │
└───────────────────────────┘
```

---

# 30. Example End-to-End Scenario

Consider a synthetic prototype scenario.

### Requirements

```text
Location A → 300 units
Location B → 250 units
Location C → 200 units
```

Total:

```text
750 units
```

### Vehicle

```text
Vehicle V-001
Capacity = 1000 units
```

### Route Status

```text
Depot → A → B → C
```

is available in the simulated scenario.

The optimizer evaluates the available constraints and generates a candidate plan.

If a simulated constraint changes:

```text
A → B route unavailable
```

the optimization input is updated and the solver can be run again to evaluate an alternative candidate plan.

All values in this example are fictional.

---

# 31. Limitations

The prototype optimization module may have limitations such as:

* Synthetic data
* Simplified route information
* Limited vehicle types
* Limited constraints
* Simplified travel estimates
* No real-time operational integration
* Prototype-level scalability

These limitations should be clearly documented during evaluation.

---

# 32. Future Improvements

Potential future improvements include:

* More advanced routing constraints
* Time-window optimization
* Dynamic travel-time estimation
* Multi-depot optimization
* Better scenario comparison
* Improved visualization
* Larger synthetic datasets
* More extensive optimization benchmarking

Any future feature should be evaluated using appropriate test data.

---

# 33. Summary

The RASAD-AI Route Optimization module connects predicted logistics requirements with delivery planning.

The complete process is:

```text
Forecast
   ↓
Risk
   ↓
Priority
   ↓
Requirements
   ↓
Vehicles
   ↓
Constraints
   ↓
Optimization
   ↓
Candidate Plan
   ↓
Validation
   ↓
Human Review
```

The module is designed to demonstrate how mathematical optimization can assist logistics planning while keeping the final decision with an authorized human user.

The public prototype should use synthetic or authorized information and must not expose sensitive operational routes or logistics data.

