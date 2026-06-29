#  E-Commerce Sales Data Analysis using Python

A simple data analysis project that demonstrates how to clean, analyze, and visualize an E-Commerce sales dataset using **Python**, **Pandas**, **NumPy**, and **Matplotlib**.

---

##  Project Overview

This project performs the following tasks:

- Loads an E-Commerce sales dataset
- Cleans missing and duplicate data
- Calculates revenue for each order
- Performs statistical analysis
- Identifies top-performing products
- Analyzes monthly sales trends
- Visualizes sales using charts
- Generates a project summary

---

##  Features

- ✅ Data Cleaning
- ✅ Missing Value Handling
- ✅ Duplicate Removal
- ✅ Revenue Calculation
- ✅ Statistical Analysis
- ✅ Monthly Sales Analysis
- ✅ Category-wise Revenue Analysis
- ✅ Product Revenue Share
- ✅ Customer Age Distribution
- ✅ Top Cities by Revenue
- ✅ Best Selling Product
- ✅ Customer Rating Analysis
- ✅ Data Visualization

---

##  Project Structure

```
ECommerce-Sales-Analysis/
│
├── EcomSales.csv          # Dataset
├── ecommerce_analysis.py  # Python source code
├── README.md
└── screenshots/           # (Optional) Graph screenshots
```

---

##  Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib

---

##  Required Libraries

Install the required packages using pip:

```bash
pip install pandas numpy matplotlib
```

---

##  Dataset

The dataset contains information such as:

- Date
- Product
- Category
- Quantity
- Price
- Customer Age
- Rating
- City

The project automatically calculates:

```
Revenue = Quantity × Price
```

---

##  Analysis Performed

### 1. Data Cleaning

- Detects missing values
- Replaces missing numeric values with the column mean
- Replaces missing text values with "Unknown"
- Removes duplicate records

---

### 2. Revenue Calculation

Creates a new column:

```
Revenue = Quantity × Price
```

---

### 3. Statistical Analysis

Calculates:

- Average Sales
- Median Revenue
- Standard Deviation

---

### 4. Product Analysis

Finds:

- Top Performing Products
- Best Selling Product

---

### 5. Sales Trend Analysis

Displays monthly revenue using a line chart.

---

### 6. Category Analysis

Shows category-wise revenue using a bar chart.

---

### 7. Revenue Share

Displays product contribution using a pie chart.

---

### 8. Customer Analysis

Shows customer age distribution using a histogram.

---

### 9. City Analysis

Displays Top 5 cities based on revenue.

---

### 10. Rating Analysis

Calculates average customer rating.

---

##  Visualizations

The project generates:

-  Monthly Sales Trend
-  Category-wise Revenue
-  Product Revenue Share
-  Customer Age Distribution

---

##  How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/ECommerce-Sales-Analysis.git
```

2. Navigate to the project folder

```bash
cd ECommerce-Sales-Analysis
```

3. Install dependencies

```bash
pip install pandas numpy matplotlib
```

4. Place the dataset (`EcomSales.csv`) inside the project folder.

5. Run the program

```bash
python ecommerce_analysis.py
```

---

##  Sample Output

```
DATASET PREVIEW

MISSING VALUES

Duplicates Removed: 3

STATISTICAL ANALYSIS

Average Sales : 4200.56
Median Revenue : 3900.00
Standard Deviation : 1125.43

TOP PERFORMING PRODUCTS

Laptop
Phone
Tablet

PROJECT SUMMARY

Total Orders : 500
Total Revenue : 2105000
Average Rating : 4.3
```

---

##  Learning Outcomes

This project demonstrates:

- Data Cleaning
- Data Manipulation
- Data Analysis
- Data Visualization
- Statistical Computation
- Python Programming
- Pandas Operations
- NumPy Functions
- Matplotlib Charts

---

##  Future Improvements

- Interactive Dashboard using Streamlit
- Sales Forecasting using Machine Learning
- Export reports to Excel/PDF
- Database Integration (MySQL/MongoDB)
- Interactive charts using Plotly
- Customer Segmentation
- Profit Analysis
- Web Application using Flask or Django

---

##  Author

**Kanishk A M**

GitHub: https://github.com/kanishk-am

---
