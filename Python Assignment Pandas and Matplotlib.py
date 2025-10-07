# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Task 1: Load and Explore Dataset
# -----------------------------
# Load dataset (Iris dataset CSV from seaborn)
df = sns.load_dataset("iris")  # If you have your own CSV, use pd.read_csv("your_file.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Check dataset info and data types
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Clean dataset if necessary (no missing values in this dataset)
# Example of filling missing values if any:
# df.fillna(df.mean(), inplace=True)

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------
# Statistical summary of numerical columns
print("\nStatistical summary of numerical columns:")
print(df.describe())

# Group by species and calculate mean of numerical columns
grouped = df.groupby('species').mean()
print("\nMean values by species:")
print(grouped)

# Observations from analysis
print("\nObservations:")
print("- Setosa species generally has smaller sepal and petal dimensions.")
print("- Versicolor and Virginica show gradual increases in measurements.")
print("- No missing values, dataset is clean.")

# -----------------------------
# Task 3: Data Visualization
# -----------------------------

# 1️⃣ Line chart (example: sepal_length trend by index)
plt.figure(figsize=(8,5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['sepal_length'], label=species)
plt.title("Sepal Length Trend by Species")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.legend()
plt.show()

# 2️⃣ Bar chart (average petal_length per species)
avg_petal_length = df.groupby('species')['petal_length'].mean()
plt.figure(figsize=(6,5))
avg_petal_length.plot(kind='bar', color=['skyblue','orange','green'])
p
