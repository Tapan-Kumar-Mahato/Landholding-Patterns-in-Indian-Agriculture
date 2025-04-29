#📊 Landholding Patterns in Indian Agriculture
This project explores landholding data in Indian agriculture using Python. It emphasizes robust data cleaning and generates insightful visualizations to better understand operational holdings across various dimensions like land size, social groups, tenancy types, and regional patterns.

#🔍 Data Cleaning Process
The dataset was thoroughly preprocessed with the following steps:

Standardized column names: Removed whitespace and special characters; converted to lowercase for consistency.

Replaced placeholders: Unified missing value indicators (NA, NaN, -, and empty strings) to NaN.

Removed duplicates and irrelevant rows: Dropped rows with missing state or district data and removed exact duplicates.

Converted columns to numeric: Ensured that holding and area columns were safely converted using pd.to_numeric.

Calculated summary fields:

total_operational_holdings

total_operated_area

avg_area_per_holding (average area per holding)

Final cleanup: Dropped any rows where summary columns were missing.

#📈 Visualizations Included
The project presents the following plots using matplotlib, seaborn, and squarify:

Box Plot
What it shows: Operated Area distribution across Land Size Classes.

Pie Chart
What it shows: Proportion of Holdings by Category.

Bar Chart
What it shows: Total Operational Holdings grouped by Social Group Type.

Line Plot
What it shows: Average Operated Area across different Land Size Classes.

Heatmap
What it shows: Top 10 Indian States by Average Operated Area.

Treemap
What it shows: Distribution of Holding Types (labels are human-readable and compact).

#🧰 Libraries Used
pandas – Data loading and preprocessing

numpy – Numerical operations

matplotlib & seaborn – Visualization and plotting

squarify – Treemap visualization

#🚀 Project Outcome
This project showcases how clear data processing and professional visualizations can turn raw agricultural statistics into actionable insights. The analysis reveals key trends in land ownership, operational fragmentation, and regional differences in holding patterns.

