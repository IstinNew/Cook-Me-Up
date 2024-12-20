# Cook-Me-Up: Simplifying Culinary Delights with Data 🍳📊

Welcome to Cook-Me-Up! This project aims to analyze and organize cooking recipes using data analysis (Python, BigQuery SQL, Looker Studio etc.) and machine learning techniques. Our goal is to simplify meal preparation and offer users a comprehensive database of culinary delights.

### Updates
This project is a work in progress and will be updated in real-time. Stay tuned for the latest enhancements and features!

## Overview

**Project Name**: Cook-Me-Up: Simplifying Culinary Delights with Data  
**Tools and Technologies**: Python, BigQuery SQL, Looker Studio, Machine Learning  
**Dataset**: [Indian Food 101](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101)  
**Project Duration**: December 16, 2024 - January 16, 2025 (excluding weekends, Xmas + new year-end vacations)

## Objectives

- Analyze and organize cooking recipes
- Provide easy-to-follow instructions, ingredients, and cooking times
- Use Unsupervised Machine Learning techniques (e.g., Clustering)
- Develop interactive visualizations using Looker Studio

## Highlights

- **Data Collection and Cleaning**: Efficiently collected and cleaned the dataset to ensure accuracy.
- **Feature Engineering**: Extracted relevant features from the dataset for better analysis.
- **Machine Learning Models**: Implemented clustering algorithms to categorize recipes.
- **Interactive Dashboards**: Created user-friendly dashboards using Looker Studio for easy data visualization.

## Challenges

- Handling missing values and inconsistencies in the dataset.
- Ensuring the machine learning models accurately categorize recipes.
- Developing interactive and intuitive visualizations.

## Folder Structure

```plaintext
Cook-Me-Up/
│
├── data/
│   ├── raw/
│   │   └── indian_food.csv        #CSV file from Kaggle API Call
│   ├── processed/
│   │   └── cleaned_data.csv       #CSV file as a Result of Data Cleaning
│   └── BigQuery/
│       └── bigquery_output.csv    #CSV file as a Result of BiqQuerySQL
│
├── notebooks/
│   ├── data_cleaning.py           #Documents the data cleaning process
│   ├── data_exploration.py        #Level 1 dataset EDA Python libraries Pandas, Numpy, Matplotlib, Seaborn
│   └── data_visualization.py      #Level 2 dataset EDA Seaborn, machine learning (Clustering etc.), input to Looker Studio
│
├── scripts/ 
│   ├── bigquery_eda.sql           #SQL script for initial exploratory data analysis using BigQuery
│   ├── bigquery_analysis.sql      #SQL script for more in-depth analysis, meaningful insights using BigQuery
│   └── visualization.sql          #SQL script for generating visualizations and input to Looker Studio
│
├── reports/
│   ├── EDA_report.md              #Markdown file documenting the exploratory data analysis
│   ├── results.md                 #Markdown file documenting the results of the analysis
│   └── final_presentation         #Folder containing the final presentation materials
│
├── README.md
├── INSTRUCTIONS.md
├── LICENSE


### Prerequisites

- Python 3.x
- BigQuery account
- Looker Studio account

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
- [WBS Coding School](https://github.com/WBSCodingSchool) for the support and guidance.
- Kaggle for providing the dataset.
- All contributors to this project.  
