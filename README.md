# 📊 Landholding Patterns in Indian Agriculture

This project explores landholding data from Indian agriculture using Python. It focuses on **cleaning real-world agricultural datasets** and using **visual analytics** to uncover key insights related to the size, type, and distribution of land holdings across states, social groups, and operational modes.

---

## 🔍 Data Cleaning Process

Real-world datasets are often messy. This project includes a careful data cleaning pipeline to ensure accurate analysis:

- **Standardized column names**: Column names were cleaned by removing special characters and extra spaces, and converting everything to lowercase for consistency.
- **Replaced placeholders**: Missing values marked as `"NA"`, `"NaN"`, `"-"`, or empty strings were standardized using `NaN` (Not a Number), which makes it easier to handle missing data.
- **Removed duplicates and irrelevant rows**: Any duplicate records were dropped, along with rows missing essential location details like `state` or `district`.
- **Converted data types**: Key columns representing the number of holdings and operated area were converted to numeric types using `pd.to_numeric()`, handling errors safely.
- **Created summary fields**:
  - `total_operational_holdings`: Sum of various types of holdings per record.
  - `total_operated_area`: Total area operated, summing across holding types.
  - `avg_area_per_holding`: A ratio indicating the average land per holding.
- **Dropped invalid rows**: After calculations, rows missing crucial totals were removed to avoid skewed results.

---

## 📈 Visualizations Included

Data visualization helps in simplifying and communicating complex datasets. This project uses multiple types of plots to explore the data from different angles:

- ### 📦 Box Plot  
  **Purpose**: Shows the distribution (spread, median, outliers) of total operated area by land size class.  
  **Insight**: Helps identify variation in land operation sizes across small, medium, and large holdings.

- ### 🥧 Pie Chart  
  **Purpose**: Displays the proportion of different holding categories (e.g., wholly owned, leased-in).  
  **Insight**: Understands which type of holding dominates the data.

- ### 📊 Bar Chart  
  **Purpose**: Compares total operational holdings across different social groups (e.g., SC, ST, OBC).  
  **Insight**: Reveals disparities in land ownership among social categories.

- ### 📈 Line Plot  
  **Purpose**: Shows how the average operated area changes with different land size classes.  
  **Insight**: Detects trends or patterns—e.g., do larger holdings always operate more land?

- ### 🌡️ Heatmap  
  **Purpose**: Highlights the top 10 states with the highest average operated area using color intensity.  
  **Insight**: Spot regional patterns in land operation efficiency.

- ### 🔳 Treemap  
  **Purpose**: Visualizes the relative size of each holding type in a compact, space-efficient format.  
  **Insight**: Makes it easy to compare the dominance of different types of holdings.

---

## 🧰 Libraries Used

- **pandas** – For reading, cleaning, and analyzing data tables  
- **numpy** – For numerical operations and array handling  
- **matplotlib & seaborn** – For generating all plots and visualizations  
- **squarify** – For drawing treemaps, which are not directly supported by seaborn

---

## 🚀 Project Outcome

This project demonstrates how a **well-structured data pipeline** and **insightful visualizations** can transform raw agricultural data into meaningful insights. The analysis brings out patterns in:

- Land distribution across size classes
- Social inequalities in landholding
- Differences between states and regions
- Types of tenancy and operation modes in Indian agriculture

These findings can be valuable for researchers, policymakers, and data analysts working in the agricultural or rural development sectors.

---

