import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("EcomSales.csv")

print("\nDATASET PREVIEW")
print(df.head())


print("\nMISSING VALUES")
print(df.isnull().sum())

# Fill missing numeric values with mean
numeric_cols = ["Quantity", "Price", "Customer_Age", "Rating"]

for col in numeric_cols:
    if col in df.columns:
        df[col].fillna(df[col].mean(), inplace=True)

# Fill missing text values
text_cols = ["Product", "Category", "City"]

for col in text_cols:
    if col in df.columns:
        df[col].fillna("Unknown", inplace=True)

# Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)

print(f"\nDuplicates Removed: {before - after}")



df["Revenue"] = df["Quantity"] * df["Price"]

print("\nDATASET WITH REVENUE")
print(df.head())


revenue = np.array(df["Revenue"])

average_sales = np.mean(revenue)
median_revenue = np.median(revenue)
std_revenue = np.std(revenue)

print("\nSTATISTICAL ANALYSIS")
print("Average Sales:", average_sales)
print("Median Revenue:", median_revenue)
print("Standard Deviation:", std_revenue)



top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP PERFORMING PRODUCTS")
print(top_products)



df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.strftime("%b")



monthly_sales = df.groupby("Month")["Revenue"].sum()

month_order = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

monthly_sales = monthly_sales.reindex(month_order).dropna()

plt.figure(figsize=(8,5))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()


category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
plt.bar(
    category_revenue.index,
    category_revenue.values
)

plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.show()


product_share = (
    df.groupby("Product")["Revenue"]
    .sum()
)

plt.figure(figsize=(8,8))
plt.pie(
    product_share.values,
    labels=product_share.index,
    autopct="%1.1f%%"
)

plt.title("Product Revenue Share")
plt.show()


plt.figure(figsize=(8,5))
plt.hist(
    df["Customer_Age"],
    bins=10
)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()



city_sales = (
    df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP 5 CITIES BY REVENUE")
print(city_sales.head())


best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nBEST SELLING PRODUCT")
print(best_product.head(1))


avg_rating = df["Rating"].mean()

print("\nAVERAGE CUSTOMER RATING")
print(round(avg_rating, 2))


print("\nPROJECT SUMMARY")
print("-----------------------------")
print("Total Orders      :", len(df))
print("Total Revenue     :", df["Revenue"].sum())
print("Average Sales     :", round(average_sales, 2))
print("Median Revenue    :", round(median_revenue, 2))
print("Std Deviation     :", round(std_revenue, 2))
print("Average Rating    :", round(avg_rating, 2))
print("-----------------------------")
