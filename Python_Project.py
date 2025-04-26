import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import squarify

# ---------------------------------- 
#  Load the dataset
# ----------------------------------
print("Step 1: Loading the dataset...")
file_path = "NDAP_REPORT_7171.csv"
df = pd.read_csv(file_path, na_values=["NA", "NaN", "-", ""])
print(f"Dataset loaded with shape: {df.shape}")
print("First 5 rows:\n", df.head(5))
print("\n")

# ---------------------------------- 
# Cleaning column names
# ----------------------------------
print("Step 2: Cleaning column names...")
df.columns = df.columns.str.strip().str.lower().str.replace('[^a-z0-9_]', '_', regex=True)
print("Columns cleaned. New column names:\n", df.columns.tolist())
print("\n")

# ----------------------------------
#  Droping rows with missing location info
# ----------------------------------
print("Step 3: Dropping rows with missing state or district info...")
initial_rows = df.shape[0]
df.dropna(subset=['state', 'district'], inplace=True)
df.drop_duplicates(inplace=True)
print(f"Removed {initial_rows - df.shape[0]} rows. Remaining rows: {df.shape[0]}")
print("\n")

# ----------------------------------
#  Defining column groups and convert numeric
# ----------------------------------
print("Step 4: Converting numeric columns...")

holdings_columns = [
    'wholly_owned_and_self_operated_holdings',
    'wholly_leased_in_holdings',
    'wholly_otherwise_operated_holdings',
    'partly_owned_and_partly_leased_in_holdings',
    'partly_owned_and_partly_otherwise_operated_holdings',
    'partly_leased_in_and_partly_otherwise_operated_holdings',
    'partly_owned_partly_leased_in_and_partly_otherwise_operated_holdings'
]

area_columns = [
    'area_of_wholly_owned_and_self_operated_holdings',
    'area_of_wholly_leased_in_holdings',
    'area_of_wholly_otherwise_operated_holdings',
    'owned_area_of_partly_owned_and_partly_leased_in_holdings',
    'owned_area_of_partly_owned_and_partly_otherwise_operated_holdings',
    'leased_in_area_of_partly_leased_in_and_partly_otherwise_operated_holdings',
    'operated_area_of_partly_owned_partly_leased_in_and_partly_otherwise_operated_holdings'
]

holdings_columns = [col for col in holdings_columns if col in df.columns]
area_columns = [col for col in area_columns if col in df.columns]

df[holdings_columns + area_columns] = df[holdings_columns + area_columns].apply(pd.to_numeric, errors='coerce')
print("Conversion complete.\n")

# ----------------------------------
#  Creating summary columns
# ----------------------------------
print("Step 5: Creating summary columns...")
df['total_operational_holdings'] = df[holdings_columns].sum(axis=1)
df['total_operated_area'] = df[area_columns].sum(axis=1)
df['avg_area_per_holding'] = df['total_operated_area'] / df['total_operational_holdings']
before = df.shape[0]
df.dropna(subset=['total_operational_holdings', 'total_operated_area'], inplace=True)
print(f"Dropped {before - df.shape[0]} rows with missing totals.\n")

# ----------------------------------
#  Displaying cleaned sample data
# ----------------------------------
print("Step 6: Sample Cleaned Rows\n")
selected_columns = [
    'state', 'district', 'land_area_size', 'social_group_type',
    'total_operational_holdings', 'total_operated_area', 'avg_area_per_holding'
]
print(df[selected_columns].head(10).to_string(index=False))
print("\n")

# ----------------------------------
#  Visualizations
# ----------------------------------
sns.set(style="whitegrid")

# Box Plot
if 'land_area_size' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='land_area_size', y='total_operated_area')
    plt.title('Box Plot: Operated Area by Land Size Class')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Pie Chart
if 'category_of_holdings' in df.columns:
    category_counts = df['category_of_holdings'].value_counts()
    if not category_counts.empty:
        plt.figure(figsize=(8, 8))
        plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Pie Chart: Category of Holdings Distribution')
        plt.tight_layout()
        plt.show()

# Bar Chart
if 'social_group_type' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='social_group_type', y='total_operational_holdings', estimator='sum', errorbar=None)
    plt.title('Bar Chart: Operational Holdings by Social Group')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Line Plot
if 'land_area_size' in df.columns:
    land_avg = df.groupby('land_area_size')['total_operated_area'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=land_avg, x='land_area_size', y='total_operated_area', marker='o')
    plt.title('Line Plot: Avg Operated Area by Land Size')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Heatmap
if 'state' in df.columns:
    state_avg = df.groupby('state')['total_operated_area'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 4))
    sns.heatmap(state_avg.to_frame().T, cmap="YlGnBu", annot=True, fmt='.1f')
    plt.title('Heatmap: Top 10 States by Avg Operated Area')
    plt.tight_layout()
    plt.show()

# Treemap
if holdings_columns:
    type_sum = df[holdings_columns].sum()
    type_sum = type_sum[type_sum > 0]
    labels = [f"{col.replace('_', ' ').title()}\n({int(val)})" for col, val in type_sum.items()]
    plt.figure(figsize=(14, 7))
    squarify.plot(sizes=type_sum.values, label=labels, alpha=0.85)
    plt.title('Treemap: Holding Type Distribution')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

print("Final Output: Dataset cleaned, summarized, and visualized successfully.")
