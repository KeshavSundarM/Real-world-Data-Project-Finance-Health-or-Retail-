# Task 4 – Real-world Data Project
## Retail Sales Analysis

### 1. Project Overview
This project performs an end-to-end analysis of a retail sales dataset. The objective is to understand sales, profitability, regional performance, product categories, sales channels, and discount behavior.

### 2. Dataset
The dataset contains Order Date, Region, Category, Channel, Customer Type, Units Sold, Unit Price, Discount, Sales, Cost, and Profit. Missing values and duplicate records are included to demonstrate practical cleaning.

### 3. Data Cleaning
- Load data using Pandas.
- Convert order dates.
- Inspect missing values and duplicates.
- Fill missing categorical values with the mode.
- Fill missing numerical values with the median.
- Remove duplicate records.
- Create Month and Profit Margin variables.

### 4. Analysis
The project performs descriptive statistics, regional analysis, product-category analysis, channel comparison, monthly sales trends, correlation analysis, and discount-versus-profit analysis.

### 5. Key Results
In the generated dataset:
- **Top category by sales:** Electronics
- **Top region by sales:** South
- **Top sales channel by sales:** Online

The analysis also compares profitability across regions and categories and examines how discounts relate to profit.

### 6. Business Insights
1. Product categories contribute differently to total sales, so inventory and marketing can be prioritized according to category performance.
2. Regional performance varies, allowing region-specific business strategies.
3. Online and store channels can be compared to guide channel investment.
4. Discount levels should be monitored because excessive discounting may reduce profit.
5. Monthly trends can support inventory, promotions, and staffing decisions.

### 7. Visualizations
- Monthly sales trend
- Sales by product category
- Profit by region
- Sales by channel
- Discount vs profit
- Correlation matrix

### 8. Conclusion
This project demonstrates an end-to-end real-world data-analysis workflow from data cleaning to business insights and visual reporting. It can be extended to sales forecasting, customer segmentation, demand prediction, and profit optimization.

### 9. Technologies
Python, Pandas, NumPy, Matplotlib, Jupyter Notebook.
