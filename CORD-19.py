Step 1: Install Required Packages
pip install pandas matplotlib seaborn streamlit wordcloud

Step 2: Load and Explore the Dataset
# Import libraries
import pandas as pd

# Load the dataset
df = pd.read_csv("metadata.csv")

# Quick overview
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Data types and missing values
print("\nDataset Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Convert publication date to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Generate basic statistics
print("\nStatistics of numerical columns:")
print(df.describe())

Step 3: Data Cleaning
# Handle missing publication dates
df = df.dropna(subset=['publish_time'])

# Fill missing abstracts with empty string
df['abstract'] = df['abstract'].fillna("")

# Optional: Create abstract word count column
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))

Step 4: Basic Data Analysis
# Papers by year
year_counts = df['year'].value_counts().sort_index()
print("\nPapers per year:")
print(year_counts)

# Top journals
top_journals = df['journal'].value_counts().head(10)
print("\nTop 10 journals:")
print(top_journals)

# Most frequent words in titles
from collections import Counter
import re

all_titles = ' '.join(df['title'].dropna())
words = re.findall(r'\w+', all_titles.lower())
common_words = Counter(words).most_common(10)
print("\nMost common words in titles:", common_words)

Step 5: Visualizations
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 1. Publications over time
plt.figure(figsize=(10,5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# 2. Top journals
plt.figure(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
plt.title("Top 10 Journals")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()

# 3. Word cloud of titles
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# 4. Distribution of abstract word counts
plt.figure(figsize=(8,5))
plt.hist(df['abstract_word_count'], bins=30, color='green', edgecolor='black')
plt.title("Distribution of Abstract Word Counts")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.show()

Step 6: Simple Streamlit Application

Create a file app.py:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# Load data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract'] = df['abstract'].fillna("")
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers interactively")

# Interactive year filter
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020,2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show basic stats
st.write(f"Number of papers in selected range: {filtered_df.shape[0]}")

# Show sample of data
st.dataframe(filtered_df[['title','journal','year']].head(10))

# Publications over time chart
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Word cloud of titles
all_titles = ' '.join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig2, ax2 = plt.subplots(figsize=(12,6))
ax2.imshow(wordcloud, interpolation='bilinear')
ax2.axis('off')
st.pyplot(fig2)


Run your Streamlit app:

streamlit run app.py
