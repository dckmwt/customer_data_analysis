# customer_data_analysis
Data analysis project showcasing customer behavior analysis using python , sql and power bi  
# Customer Behaviour Analysis

## Overview

This project focuses on analyzing customer shopping behaviour to understand purchasing patterns, customer preferences, discount usage, subscription trends, and revenue contribution.

The project uses **Python, SQL (MySQL), and Power BI** to clean and transform raw customer data, perform exploratory data analysis (EDA), answer business questions, and present insights through an interactive dashboard.

## Dataset

The dataset contains customer shopping information, including:

- Customer ID, age, and gender
- Item purchased and product category
- Purchase amount, size, and color
- Season and review rating
- Subscription status
- Discount applied and promo code used
- Shipping type and payment method
- Frequency of purchases and previous purchases

**Source file:** `customer_shopping_behavior_missing.csv`

## Tools & Technologies

- **Python:** Data loading, cleaning, transformation, and EDA
- **Pandas:** Data manipulation and analysis
- **SQL (MySQL):** Business queries and data analysis
- **SQLAlchemy:** Connecting Python with MySQL
- **Power BI:** Interactive dashboard and visualization
- **VS Code:** Python development environment

## Project Workflow

### 1. Data Loading & EDA

- Loaded the dataset using Pandas.
- Inspected the first few records and dataset structure.
- Analyzed data types and summary statistics.
- Identified missing values and examined data quality.

### 2. Data Cleaning & Transformation

- Handled missing review ratings using the median rating within each product category.
- Standardized column names to lowercase and replaced spaces with underscores.
- Renamed `purchase_amount_(usd)` to `purchase_amount`.
- Created an `age_group` column using age-based quartiles.
- Converted purchase frequency categories into numerical day intervals.
- Removed the redundant `promo_code_used` column because it duplicated the information in `discount_applied`.

### 3. SQL Analysis Using MySQL

Loaded the cleaned dataset into MySQL and used SQL queries to investigate key business questions.

The analysis included:

- Total revenue by gender
- Customers using discounts and spending at or above the average purchase amount
- Top-rated products and product categories
- Average purchase amount by shipping type
- Spending and revenue comparison between subscribers and non-subscribers
- Discount usage percentage by product
- Customer segmentation into new, returning, and loyal customers
- Product purchase rankings within categories
- Subscription behaviour among repeat buyers
- Revenue contribution by age group

SQL techniques included `GROUP BY`, aggregate functions, subqueries, `CASE` statements, Common Table Expressions (CTEs), and window functions.

### 4. Power BI Dashboard

Built a dashboard to present customer behaviour and purchasing insights in an easy-to-understand visual format.

The dashboard can be used to explore:

- Revenue and purchasing trends
- Customer demographics and age groups
- Product preferences and review ratings
- Discount usage and subscription behaviour
- Shipping preferences and purchase frequency

*Add a screenshot of your Power BI dashboard here.*

## Key Results & Insights

The project provides a structured approach to understanding customer shopping behaviour and supports analysis of:

- **Revenue patterns:** Compare purchasing contributions across customer demographics.
- **Customer segmentation:** Identify new, returning, and loyal customer groups.
- **Discount effectiveness:** Examine discount usage and spending patterns.
- **Subscription behaviour:** Compare spending between subscribers and non-subscribers.
- **Product performance:** Evaluate product popularity and customer review ratings.
- **Purchasing preferences:** Explore shipping choices and purchase frequency.

The findings can help businesses better understand their customers and make data-informed decisions about marketing, customer retention, and product strategy.

*Note: Actual numerical findings should be added after reviewing the SQL query outputs and Power BI dashboard.*

## Project Structure

```text
Customer-Behaviour-Analysis/
│
├── project.py
├── customer_behaviour_sql_querry.sql
├── customer_shopping_behavior_missing.csv
├── README.md
│
└── dashboard/
    └── customer_behaviour_dashboard.png
```

*The dashboard folder and screenshot are optional. Update the structure to match the files in your GitHub repository.*

## How to Run

### Prerequisites

Install the following:

- Python 3.x
- MySQL Server
- Visual Studio Code
- Power BI Desktop

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd Customer-Behaviour-Analysis
```

### Step 2: Install Python Libraries

```bash
pip install pandas sqlalchemy mysql-connector-python
```

### Step 3: Prepare the Dataset

Place `customer_shopping_behavior_missing.csv` in the appropriate project directory and update the file path in `project.py` if required.

### Step 4: Configure MySQL

Create the database:

```sql
CREATE DATABASE IF NOT EXISTS customer_behavior;
```

Update the MySQL connection settings in `project.py` with your own local credentials. Keep passwords out of the public repository.

### Step 5: Run the Python Script

Open the project in VS Code and execute:

```bash
python project.py
```

The script loads, cleans, and transforms the dataset before uploading it to the `cleaned_shopping_data` table in MySQL.

### Step 6: Execute SQL Queries

Open `customer_behaviour_sql_querry.sql` in your MySQL client, select the `customer_behavior` database, and execute the queries to perform the business analysis.

### Step 7: Open the Power BI Dashboard

Open the Power BI report in Power BI Desktop, configure the data connection if needed, and refresh the data to explore the visualizations.

## Conclusion

This project demonstrates an end-to-end data analytics workflow, from raw data preparation and exploratory analysis to SQL-based business analysis and interactive Power BI reporting.

It showcases practical skills in **Python, Pandas, MySQL, data cleaning, EDA, business problem-solving, and data visualization**.

## Author

**Your Name  :- Dharmchand Kumawat**

Aspiring Data Analyst

Skills: Python | SQL | MySQL | Power BI | Pandas | EDA
