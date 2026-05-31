import pandas as pd
df = pd.read_csv(r"c:\Users\lalit\Downloads\Walmart_Sales.csv")

# Checking Dataset
print(df.head())
print(df.info())
print(df.describe())

# Checking for null values
print(df.isnull().sum())

# Checking for duplicates
print(df.duplicated().sum())

# Data types of columns
print(df.dtypes)

# Converting 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Turning column names to lower case
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()

# Rounding of values
df['weekly_sales'] = df['weekly_sales'].round(2)
df['fuel_price'] = df['fuel_price'].round(2)

# Checking the dataset
print(df.head())

# Saving the cleaned dataset
df.to_csv("cleaned_walmart_sales.csv", index=False)
print("Data cleaned and saved!")