Seeds created artificially in seed_gen.py
# Insights
Top customer: Kateryna Hrytsenko -> 3965 UAH from 9 orders
Revenue trend: from march till july revenue from 250 to 7695
Couriers: Denys Zaitsev fastest




# Practical Assignment: Build Your Own dbt Project for a Business

## Goal

Build a complete **dbt project** for a business scenario of your choice using **DuckDB** as the warehouse.

You must design and implement a small analytical platform using **CSV files in `seeds/`** as the source data, transform the data through **raw**, **stage**, and **mart** layers, and produce business-ready insights.

Your solution must be structured, tested, and explained using correct **dbt** and **data warehousing** terminology.

---

## Business Context

Choose any business domain, for example:

- e-commerce
- food delivery
- hospital
- school
- banking
- streaming platform
- logistics
- hotel booking
- fitness club
- marketplace

You must clearly describe:

- what business you selected
- what data entities exist
- what business questions your project answers

---

## Technical Requirements

Your project must satisfy **all** requirements below.

### 1. Use DuckDB
- The project must run on **DuckDB**.
- Configure the project correctly so that models can be built locally.

### 2. Source Data in Seeds
- All initial data must be stored as **CSV files** inside the `seeds/` folder.
- Use enough source tables to support your business scenario.

### 3. Minimum 20 dbt Models
Create **at least 20 models** in total.

Your project must include the following layers:

- **raw layer**
- **stage layer**
- **mart layer**

You may create more than 20 models.

### 4. At Least 5 Incremental Models
You must create **at least 5 incremental models**.

These models should demonstrate that you understand:

- incremental materialization
- unique keys
- filtering new or changed records
- incremental logic in dbt

### 5. Add Incremental Predicate Logic
At least one incremental model must include an **incremental predicate**.

You must be able to explain:

- why this predicate is needed
- what problem it solves
- what tradeoff it introduces

### 6. Add at Least 1 Custom Macro (Optional + 2.5)
Create **at least 1 macro**.

The macro must be used in your project in a meaningful way.  
Examples:

- standardize text fields
- generate surrogate keys
- calculate business status labels
- reusable date filtering logic
- reusable null handling logic

You must explain:

- what the macro does
- why a macro is better than copying SQL repeatedly

### 7. Use Window Functions
You must use **window functions** in at least **2 models**.

Examples:

- `row_number()`
- `rank()`
- `dense_rank()`
- `lag()`
- `lead()`
- `sum() over (...)`
- `avg() over (...)`

Use them for a real business purpose such as:

- ranking customers
- identifying latest orders
- calculating running totals
- detecting status changes
- measuring customer retention

### 8. Add Tests
Add dbt tests to validate your models.

Include both:

- **generic tests**
- **custom or singular tests** if appropriate

At minimum, test:

- primary key uniqueness
- not null constraints
- accepted values
- relationships between tables

### 9. Follow a Style Guide
Your project must follow a consistent SQL and dbt style guide.

At minimum:

- meaningful model names
- one purpose per model
- clear CTE names
- consistent formatting
- aliases for business-readable column names
- comments or descriptions where useful
- organized folder structure
- YAML documentation for models

### 10. Provide Data Insights
Create a short analytical section that shows **useful business insights** from your marts.

Examples:

- top customers by revenue
- most profitable product category
- repeat purchase behavior
- monthly revenue trend
- churned users
- delayed deliveries
- best-performing city or region

The insights must come from your transformed models, not from raw seed files directly.

### 11. Explain Your Solution
Be prepared to explain your solution using correct terminology, including:

- seed
- source
- model
- materialization
- incremental model
- macro
- test
- staging layer
- mart layer
- window function
- surrogate key
- grain
- lineage
- dependency
- data quality

---

## Assignment Evaluation

| Component | Description | Points |
|---|---|---|
| DuckDB Configuration | Project runs locally using DuckDB and is correctly configured. | 0.5 |
| Seeds (CSV Source Data) | Source data is stored in `seeds/` as CSV files and supports the chosen business scenario. | 0.5 |
| Project Architecture | Clear layered structure: **raw**, **stage**, and **mart** layers with logical dependencies between models. | 1 |
| Minimum 20 dbt Models | At least **20 dbt models** implemented with meaningful transformations. | 1 |
| Incremental Models | At least **5 incremental models** implemented with correct incremental logic and unique keys. | 1 |
| Incremental Predicate | At least **one incremental predicate** implemented and correctly explained. | 0.5 |
| Window Functions | Window functions used in at least **2 models** for meaningful analytical purposes. | 0.5 |
| Data Tests | dbt tests implemented (e.g., `not_null`, `unique`, `relationships`, `accepted_values`). | 0.5 |
| Style Guide and Project Organization | Consistent SQL formatting, meaningful model names, clear CTE structure, proper folder organization, and YAML documentation. | 0.5 |
| Business Insights | Analytical outputs from mart models that provide useful business insights. | 0.5 |
| Solution Explanation | Student can clearly explain the architecture, model grain, transformations, and dbt concepts using correct terminology. | 0.5 |
| **Optional: Custom Macro** | At least one meaningful macro created and used in the project. | **+2.5** |
| **Theoretical Questions** | Answers to the **10 theoretical dbt questions** demonstrating understanding of key concepts. | **3** |
| **Total** |  | **10 (+2.5 optional bonus)** |

### Theoretical Questions about dbt

1. What is the purpose of dbt in a modern data stack? 
2. What is the difference between a seed, a source, and a model in dbt? 
3. What is the difference between table, view, and incremental materializations? 
4. What is the purpose of the staging layer in a dbt project? 
5. What is the difference between a dimension model and a fact model? 
6. Why are tests important in dbt, and what is the difference between generic and singular tests? 
7. What is a macro in dbt, and when should you create one? 
8. What is an incremental predicate, and how does it improve model performance? 
9. Why are window functions useful in analytics engineering? 
10. What does it mean to describe the grain of a model, and why is grain important?
