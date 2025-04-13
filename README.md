# 📊 Landholding-Patterns-in-Indian-Agriculture

This project explores agricultural holdings data using **Python**. It focuses on data cleaning and producing multiple visualizations to uncover insights into operational holdings across various categories.

---

## 🥹 Data Cleaning Steps:
- Cleaned inconsistent column names for uniformity.
- Replaced missing value placeholders (`NA`, `NaN`, `-`) with `NaN` for consistency.
- Removed any duplicate rows to ensure clean data.
- Converted holding and area columns to numeric types safely using `pd.to_numeric`.
- Dropped rows where crucial fields (`state`, `district`, total calculations) were missing.

---

## 📊 Visualizations Included:

1. **Box Plot**  
   Visualizes: Operated Area by Land Size Class.

2. **Pie Chart**  
   Visualizes: Distribution of Holdings by Category.

3. **Bar Chart**  
   Visualizes: Total Operational Holdings grouped by Social Group Type.

4. **Line Plot**  
   Visualizes: Average Operated Area across different Land Size Classes.

5. **Heatmap**  
   Visualizes: Top 10 States by Average Operated Area.

6. **Treemap**  
   Visualizes: Distribution of Holding Types (with readable, shortened labels).

---

## 📚 Libraries Used:
- `pandas` — data manipulation.
- `numpy` — numeric operations.
- `seaborn` and `matplotlib` — data visualization.
- `squarify` — treemap visualization.

---

## 🚀 Result:

This project combines clean, professional plots and strong data preparation practices to analyze landholding data. It highlights how visualizations can simplify complex data and help uncover trends and patterns.




