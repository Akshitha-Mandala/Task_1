import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\lalit\Downloads\netflix_titles.csv.zip")

# Checking the dataset
print(df.head())
print(df.info())
print(df.describe())

# Checking for null values
print(df.isnull().sum())
df = df.replace(["null", "NULL", "None", "none"], np.nan)
df = df.dropna()
df = df.drop(["description","cast"], axis=1)

# Handle missing values
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")


# listening to the unique values in the 'listed_in' column
print(df['listed_in'].unique())
df["genres"] = df["listed_in"].str.split(",").str[0]
df = df.drop("listed_in", axis=1)
df["country"] = df["country"].str.split(",").str[0]
df["director"] = df["director"].str.split(",").str[0]

# Checking for duplicates
print(df.duplicated().sum())

# Data types of columns
print(df.dtypes)

# Final Checking of the dataset
print(df.info())
print(df.head())

# Saving the cleaned dataset
df.to_csv("cleaned_netflix_titles.csv", index=False)


