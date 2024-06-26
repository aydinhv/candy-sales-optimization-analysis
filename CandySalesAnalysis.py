import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Seed for reproducibility
np.random.seed(42)

# Data Generation
dates = pd.date_range(start='2019-01-01', end='2021-12-31', freq='D')
products = ['Chocolate Bar', 'Gummy Bears', 'Caramel Chews', 'Licorice', 'Hard Candy']
regions = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide']
data = {
    'Date': np.repeat(dates, len(products)),
    'Product': np.tile(products, len(dates)),
    'Region': np.random.choice(regions, len(dates) * len(products)),
    'Quantity': np.random.randint(100, 1000, len(dates) * len(products)),
    'UnitPrice': np.random.uniform(1.0, 5.0, len(dates) * len(products)).round(2)
}
df = pd.DataFrame(data)
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Data Cleaning
df.dropna(inplace=True)  # Remove any missing values, if necessary
df = df[df['Quantity'] > 0]  # Ensure there are no zero quantity entries

# Feature Engineering
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10, 6))
sns.barplot(x='Product', y='TotalSales', data=df, estimator=sum, ci=None)
plt.title('Total Sales by Product')
plt.ylabel('Total Sales')
plt.xlabel('Product')
plt.xticks(rotation=45)
plt.show()

# Sales trends over time
monthly_sales = df.groupby(['Year', 'Month'])['TotalSales'].sum().reset_index()
monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))
plt.figure(figsize=(14, 7))
sns.lineplot(x='Date', y='TotalSales', data=monthly_sales)
plt.title('Monthly Sales Trends')
plt.ylabel('Total Sales')
plt.xlabel('Date')
plt.show()

# Save the cleaned and processed data to a CSV file
df.to_csv('ProcessedCandySalesData.csv', index=False)
