# -*- coding: utf-8 -*-
"""CMPD_Crimes_Data_EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10DHzfaxUQx4gIFanbRFj_uZV5nysqhwB
"""

# Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load crime data from a CSV file
crime_data = pd.read_csv('CMPD_Violent_Crime.csv')

print(crime_data.describe())

crime_data.head()

crime_data.info()

"""Exploratory Data Analysis (EDA)"""

# Load the dataset
df = pd.read_csv('/content/CMPD_Violent_Crime.csv')

# 1. Data Overview
print("Dataset Shape:", df.shape)  # Rows and Columns
print("\nColumns in the dataset:")
print(df.columns)  # List of column names

print("\nData Info:")
df.info()  # Information about the dataset

print("\nFirst 5 rows of the dataset:")
print(df.head())  # First few rows of the dataset

print("\nBasic Statistics (Numerical Columns):")
print(df.describe())  # Summary statistics of numerical columns

# 2. Check for Missing Data
print("\nMissing Values Count:")
print(df.isnull().sum())  # Check for missing values in the dataset

# 3. Categorical Data Analysis
print("\nUnique values in Categorical Columns:")
for col in ['ROW_TYPE', 'GEOGRAPHY', 'OFFENSE_DESCRIPTION']:
    print(f"{col}: {df[col].nunique()} unique values")

# Frequency distribution of categorical columns
for col in ['ROW_TYPE', 'GEOGRAPHY', 'OFFENSE_DESCRIPTION']:
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"Distribution of {col}")
    plt.show()

# 4. Numerical Data Analysis
print("\nDistribution of Numerical Columns:")
for col in ['CALENDAR_YEAR', 'CALENDAR_MONTH', 'OFFENSE_COUNT']:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f"Distribution of {col}")
    plt.show()

# Boxplot for numerical columns to check for outliers
for col in ['CALENDAR_YEAR', 'CALENDAR_MONTH', 'OFFENSE_COUNT']:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# 5. Correlation Analysis
# Correlation heatmap for numerical columns
corr_matrix = df[['GEOGRAPHY_ID', 'CALENDAR_YEAR', 'CALENDAR_MONTH', 'OFFENSE_COUNT', 'OBJECTID']].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# 6. Visualizing Offense Count over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='CALENDAR_YEAR', y='OFFENSE_COUNT', hue='GEOGRAPHY', ci=None)
plt.title("Offense Count Trend Over the Years by Geography")
plt.xticks(rotation=90)
plt.show()

# 7. Offense Description Analysis
# Top 10 offenses
top_offenses = df['OFFENSE_DESCRIPTION'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_offenses.values, y=top_offenses.index, palette='viridis')
plt.title("Top 10 Most Frequent Offenses")
plt.show()