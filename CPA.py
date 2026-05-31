import pandas as pd

df = pd.read_csv(r"C:\Users\lalit\Downloads\marketing_campaign.csv", sep="\t")
print(df.head())

# To know the summary of the dataset
print(df.info())

# To know the number of null values in each column
print(df.isnull().sum())

# To fill the null values in the 'Income' column with the median value of that column
df['Income'] = df['Income'].fillna(df['Income'].median())
print(df.isnull().sum())

# To check for duplicate rows in the dataset
print(df.duplicated().sum())

# To convert column names to lower cases
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()

# To convert the "date" column to datetime format
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')
print(df.dtypes)

#Standardize the values in the 'education' and 'marital_status' columns
print(df['education'].unique())
print(df['marital_status'].unique())
df['marital_status']= df['marital_status'].replace({"YOLO": "Single", "Absurd": "Single", "Alone": "Single"})

# To create a new column 'age' by calculating the age of the customers based on their year of birth
df['age'] = 2026 - df['year_birth']
print(df['age'].describe())
# removing unreasonable age values
df = df[df['age'] < 100]
print(df['age'].describe())
print(df.head())

df.to_csv("cleaned_marketing_campaign_2.csv", index=False)
print("Data cleaned and saved!")
