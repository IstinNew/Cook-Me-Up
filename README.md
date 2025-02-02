# **Cook-Me-Up: Simplifying Culinary Delights with Data 🍳📊**

Welcome to **Cook-Me-Up**! This project combines the power of data analysis, machine learning, and interactive visualizations to explore and organize cooking recipes. By analyzing an extensive Indian food dataset, we aim to simplify meal preparation and provide users with a comprehensive database of culinary delights.

---

## **🚀 Key Updates**

- **Live Streamlit App**: Explore the dataset and gain insights interactively!  
  👉 [Cook-Me-Up Streamlit App](https://cook-me-up.streamlit.app/)  

This project is a work in progress and will be updated in real-time until February 2025. Stay tuned for the latest enhancements and features!

---

## **🔍 Overview**

- **Project Name**: Cook-Me-Up: Simplifying Culinary Delights with Data  
- **Tools and Technologies**: Python, BigQuery SQL, Looker Studio, Machine Learning  
- **Dataset**: [Indian Food 101](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101)  
- **Project Duration**: December 16, 2024 - January 16, 2025 (excluding weekends, xmas + new year-end vacations)

---

## **🎯 Objectives**

- Analyze and organize cooking recipes.
- Provide easy-to-follow instructions, ingredients, and cooking times.
- Apply unsupervised machine learning techniques (e.g., Clustering).
- Develop interactive visualizations using Looker Studio.

---

## **🌟 Highlights**

- **Data Collection and Cleaning**: Efficiently collected and cleaned the dataset to ensure accuracy.  
- **Feature Engineering**: Extracted relevant features from the dataset for better analysis.  
- **Machine Learning Models**: Implemented clustering algorithms to categorize recipes.  
- **Interactive Dashboards**: Designed user-friendly dashboards using Looker Studio for easy data visualization.  

---

## **🛠️ Folder Structure**

```plaintext
Cook-Me-Up/
│
├── data/
│   ├── raw/
│   │   └── indian_food.csv        # Original CSV file from Kaggle API Call
│   ├── processed/
│   │   └── cleaned_data.csv       # CSV file as a Result of Data Cleaning
│   └── BigQuery/
│       └── bigquery_output.csv    # CSV file as a Result of BigQuery SQL
│
├── notebooks/
│   ├── data_cleaning.py           # Documents the data cleaning process
│   ├── data_exploration.py        # Level 1 dataset EDA Python libraries Pandas, Numpy, Matplotlib, Seaborn
│   └── data_visualization.py      # Level 2 dataset EDA Seaborn, machine learning (Clustering etc.), input to Looker Studio
│
├── scripts/ 
│   ├── bigquery_eda.sql           # SQL script for initial exploratory data analysis using BigQuery
│   ├── bigquery_analysis.sql      # SQL script for more in-depth analysis, meaningful insights using BigQuery
│   └── visualization.sql          # SQL script for generating visualizations and input to Looker Studio
│
├── reports/
│   ├── EDA_report.md              # Markdown file documenting the exploratory data analysis
│   ├── results.md                 # Markdown file documenting the results of the analysis
│   └── final_presentation         # Folder containing the final presentation materials
│
├── streamlit/                     # Streamlit app files (through a side branch: streamlit_deployment)
│   ├── streamlit_app.py           # application script
│   └── indian_food.csv            # raw CSV file for Streamlit app
│
├── README.md
├── INSTRUCTIONS.md
├── LICENSE
│
├── images/
│   ├── cooking_time_distribution.png
│   ├── diet_type_distribution.png
│   ├── Pair_Plot.png
│   └── ... (other images)


```
### 📋 Prerequisites

- Python 3.x
- BigQuery account
- Looker Studio account

### 📈 Results

### **Detailed Results and Reports**

- 👉 **[Exploratory Data Analysis Report](./reports/EDA_report.md)**  
  This report provides a comprehensive step-by-step exploratory data analysis of the dataset, uncovering key trends and patterns.

- 👉 **[Results Analysis Report](./reports/results.md)**  
  This document highlights the final findings and insights from the project, including the outcomes of machine learning models.

- 👉 **[Cook-Me-Up Streamlit App](https://cook-me-up.streamlit.app/)**  
  Interactively explore the dataset and visualizations via the live Streamlit app.

- 👉 **[Interactive Looker Studio Report](https://lookerstudio.google.com/reporting/77435f8b-ea4d-4201-8cf0-356d8445671e)**  
  Access detailed, interactive visualizations and insights derived from the dataset. The report includes dynamic charts, tables, and filters to enable deeper exploration.

#### Machine Learning Visualization: Pair Plot

To understand the relationships between key features of the dataset, a **Pair Plot** was generated using machine learning techniques. This visualization highlights interactions between features such as total time, number of ingredients, flavor profile, course, and region. Each cell in the pair plot matrix represents a scatter plot of two features, with one feature on the X-axis and the other on the Y-axis. The diagonal cells display the distribution of individual features.

The pair plot revealed interesting trends, such as how the total time required for recipes is distributed across different regions and how the flavor profile correlates with the number of ingredients. These insights provide valuable context for categorizing recipes and understanding regional patterns in Indian cuisine.

👉 **[View the Pair Plot](./images/Pair_Plot.png)**

All files and reports are structured in their respective subfolders for easy navigation. Explore them for detailed results and insights!

---
### 📜 License
-This project is licensed under the MIT License. See the [LICENSE](./LICENSE)  for details.
<!-- -->
### 🙏 Acknowledgments
<!-- - [WBS Coding School](https://github.com/WBSCodingSchool) for the support and guidance.-->
- [Kaggle- Indian Food 101](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101) for the dataset.
- All contributors to this project.  
