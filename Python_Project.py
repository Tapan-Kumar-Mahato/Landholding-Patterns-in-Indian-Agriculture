import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Load data 
file_path = "C:/Users/Tapan Kumar Mahato/Desktop/Projects/Python/NDAP_REPORT_7171.csv"
df = pd.read_csv(file_path, na_values=["NA", "NaN", "-", ""])

# Clean Column Names
df.columns = df.columns.str.strip().str.lower().str.replace('[^a-z0-9_]', '_', regex=True)

# Show columns for verification
print("Available Columns:\n", df.columns.tolist())

# Drop rows where important columns are missing
df.dropna(subset=['state', 'district'], inplace=True)

# Remove duplicate rows if any
df.drop_duplicates(inplace=True)

# Define holdings and area columns
possible_holdings_columns = [
    'wholly_owned_and_self_operated_holdings',
    'wholly_leased_in_holdings',
    'wholly_otherwise_operated_holdings',
    'partly_owned_and_partly_leased_in_holdings',
    'partly_owned_and_partly_otherwise_operated_holdings',
    'partly_leased_in_and_partly_otherwise_operated_holdings',
    'partly_owned_partly_leased_in_and_partly_otherwise_operated_holdings'
]

possible_area_columns = [
    'area_of_wholly_owned_and_self_operated_holdings',
    'area_of_wholly_leased_in_holdings',
    'area_of_wholly_otherwise_operated_holdings',
    'owned_area_of_partly_owned_and_partly_leased_in_holdings',
    'owned_area_of_partly_owned_and_partly_otherwise_operated_holdings',
    'leased_in_area_of_partly_leased_in_and_partly_otherwise_operated_holdings',
    'operated_area_of_partly_owned_partly_leased_in_and_partly_otherwise_operated_holdings'
]

# Step 5: Select only existing columns
holdings_columns = [col for col in possible_holdings_columns if col in df.columns]
area_columns = [col for col in possible_area_columns if col in df.columns]

# Step 6: Convert to numeric
df[holdings_columns + area_columns] = df[holdings_columns + area_columns].apply(pd.to_numeric, errors='coerce')

# Step 7: Create totals
df['total_operational_holdings'] = df[holdings_columns].sum(axis=1)
df['total_operated_area'] = df[area_columns].sum(axis=1)

# Step 8: Drop rows where totals are missing
df.dropna(subset=['total_operational_holdings', 'total_operated_area'], inplace=True)

# Visualization styling
sns.set(style="whitegrid")

# --- Box Plot ---
if 'land_area_size' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='land_area_size', y='total_operated_area')
    plt.title('Box Plot: Operated Area by Land Size Class')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Column 'land_area_size' not found for box plot.")

#  Pie Chart 
if 'category_of_holdings' in df.columns:
    category_counts = df['category_of_holdings'].value_counts(dropna=True)
    if not category_counts.empty:
        plt.figure(figsize=(8, 8))
        plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Pie Chart: Category of Holdings Distribution')
        plt.tight_layout()
        plt.show()
    else:
        print("Column 'category_of_holdings' exists but has no valid data for pie chart.")
else:
    print("Column 'category_of_holdings' not found for pie chart.")

# Bar Chart 
if 'social_group_type' in df.columns:
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x='social_group_type', y='total_operational_holdings', estimator=sum, errorbar=None)
    plt.title('Bar Chart: Holdings by Social Group')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Column 'social_group_type' not found for bar chart.")

# Line Plot 
if 'land_area_size' in df.columns:
    land_avg = df.groupby('land_area_size')['total_operated_area'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=land_avg, x='land_area_size', y='total_operated_area', marker='o')
    plt.title('Line Chart: Avg Operated Area by Land Size Class')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Column 'land_area_size' not found for line plot.")

# Heatmap 
if 'state' in df.columns:
    state_area = df.groupby('state')['total_operated_area'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(8, 6))
    sns.heatmap(state_area.to_frame().T, cmap="YlGnBu", annot=True, fmt='.2f')
    plt.title("Heatmap: Top 10 States by Avg Operated Area")
    plt.tight_layout()
    plt.show()
else:
    print("Column 'state' not found for heatmap.")

# Treemap with Clear Labels 
if holdings_columns:
    type_sum = df[holdings_columns].sum()
    filtered = type_sum[type_sum > 0]

    labels = []
    for label, value in zip(filtered.index, filtered.values):
        pretty = label.replace('_', ' ').title()
        if len(pretty) > 25:  # Shorten if label is too long
            pretty = pretty[:22] + '...'
        labels.append(f"{pretty}\n({value:,.0f})")

    plt.figure(figsize=(14, 8))
    squarify.plot(sizes=filtered.values, label=labels, alpha=0.8, text_kwargs={'fontsize':14, 'weight':'bold'})
    plt.title("Treemap: Holding Type Distribution", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
else:
    print("No valid holding columns found for treemap.")
