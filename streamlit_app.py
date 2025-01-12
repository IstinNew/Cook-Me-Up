import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os
from wordcloud import WordCloud

# Define the relative path to the dataset (for Streamlit deployment)
csv_file_path = os.path.join(os.getcwd(), 'indian_food.csv')

# Function to load the dataset
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data.fillna('Unknown', inplace=True)  # Handle missing values
    data.drop_duplicates(inplace=True)  # Remove duplicates
    data['flavor_profile'] = data['flavor_profile'].replace('-1', 'Others')
    data['state'] = data['state'].replace('-1', 'Others')
    data['region'] = data['region'].replace('-1', 'Others')
    data['cook_time'] = data['cook_time'].replace(-1, 0)
    data['prep_time'] = data['prep_time'].replace(-1, 0)
    return data

# Load data
df = load_data(csv_file_path)

# Function to generate word cloud
def create_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    st.pyplot(plt)

# Streamlit app layout
st.title("Cook-Me-Up: Indian Food Insights")
st.sidebar.title("Navigation")

# Sidebar navigation
sections = st.sidebar.radio("Sections", ["Introduction", "Interactive Data Overview", "Visualizations", "Insights"])

if sections == "Introduction":
    st.header("Introduction")
    st.write("""
    Welcome to the Cook-Me-Up project! This app provides insights into Indian food recipes using Python, Machine Learning, BigQuery, and Looker Studio.
    Navigate through the sections to explore interactive data, visualizations, and insights!
    """)
    st.markdown("""
    **Dataset Source:** [Indian Food 101 on Kaggle](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101)  
    **Conceptualized and Developed by:** Shayak Majumder  
    **Special Thanks to:** [WBS Coding School](https://www.wbscodingschool.com) for guidance and inspiration.  
    """)
    st.markdown("© 2025 Shayak Majumder. All Rights Reserved.")

    # Create word clouds for recipe titles and ingredients
    st.subheader("Word Clouds for Recipe Titles and Ingredients")
    recipe_titles = ' '.join(df['name'])
    create_wordcloud(recipe_titles, 'Common Words in Recipe Titles')
    ingredients_text = ' '.join(df['ingredients'])
    create_wordcloud(ingredients_text, 'Common Ingredients in Recipes')

elif sections == "Interactive Data Overview":
    st.header("Interactive Data Overview")
    st.write("Explore the dataset interactively using filters.")
    selected_flavor = st.selectbox("Select Flavor Profile", options=df['flavor_profile'].unique())
    selected_region = st.multiselect("Select Region(s)", options=df['region'].unique(), default=df['region'].unique())
    selected_diet = st.radio("Select Diet", options=df['diet'].unique())
    filtered_df = df[
        (df['flavor_profile'] == selected_flavor) &
        (df['region'].isin(selected_region)) &
        (df['diet'] == selected_diet)
    ]
    st.write(f"Filtered dataset ({len(filtered_df)} rows):")
    st.dataframe(filtered_df)
    st.write("Summary statistics of the filtered data:")
    st.write(filtered_df.describe())

elif sections == "Visualizations":
    st.header("Visualizations")
    st.write("Analyze the dataset through Python, Machine Learning, and Looker Studio visualizations.")
    region_selection = st.selectbox('Select Region to Display Ingredient Frequency', df['region'].unique())
    InEast, InWest, InNorth, InOthers, InNorthEast, InSouth, InCentral = [], [], [], [], [], [], []
    for row in range(len(df)):
        region = df['region'][row]
        ingredients = df['ingredients'][row].split(', ')
        if region == 'East': InEast.extend(ingredients)
        elif region == 'West': InWest.extend(ingredients)
        elif region == 'North': InNorth.extend(ingredients)
        elif region == 'North East': InNorthEast.extend(ingredients)
        elif region == 'South': InSouth.extend(ingredients)
        elif region == 'Central': InCentral.extend(ingredients)
        else: InOthers.extend(ingredients)
    all_ingredient = pd.Series(InEast + InWest + InNorth + InOthers + InNorthEast + InSouth + InCentral).unique()
    ingredient_counts = {
        'East': [InEast.count(ingredient) for ingredient in all_ingredient],
        'West': [InWest.count(ingredient) for ingredient in all_ingredient],
        'North': [InNorth.count(ingredient) for ingredient in all_ingredient],
        'Others': [InOthers.count(ingredient) for ingredient in all_ingredient],
        'North East': [InNorthEast.count(ingredient) for ingredient in all_ingredient],
        'South': [InSouth.count(ingredient) for ingredient in all_ingredient],
        'Central': [InCentral.count(ingredient) for ingredient in all_ingredient],
    }
    ingredient_per_region = pd.DataFrame(ingredient_counts, index=all_ingredient)
    ingredient_per_region['Sum'] = ingredient_per_region.sum(axis=1)
    st.subheader(f'Top 15 Ingredients in {region_selection} Region')
    ord_region = ingredient_per_region.sort_values([region_selection], ascending=False)[0:15]
    plt.figure(figsize=(12, 8), dpi=100)
    sns.barplot(x=ord_region[region_selection], y=ord_region.index, palette='Paired')
    plt.xlabel('Count')
    plt.ylabel('Ingredients')
    plt.title(f'{region_selection} Ingredient Frequency')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    st.subheader("Looker Studio Integration")
    st.write("Explore enhanced visualizations via Looker Studio below:")
    st.components.v1.iframe(
        src="https://lookerstudio.google.com/embed/reporting/77435f8b-ea4d-4201-8cf0-356d8445671e/page/mQ1cE",
        width=1200,
        height=800,
    )

elif sections == "Insights":
    st.header("Insights")
    st.write("Discover meaningful insights derived from the dataset.")

    # Key takeaways
    st.write("""
    - The **North** and **South** regions dominate the dataset in terms of the number of dishes.
    - **Preparation** and **cooking times** vary significantly, highlighting opportunities for clustering and pattern identification.
    - A diverse range of ingredients is prominent across regions, with notable overlaps between the **North** and **West** regions.
    - The dataset reveals a high prevalence of vegetarian dishes, reflecting cultural preferences in India.
    - Visualizations in Looker Studio provide additional depth to this analysis, enabling dynamic filtering and exploration.
    """)

    st.write("For a deeper dive into the results, check out the following reports:")
    st.markdown("- 👉 **[Exploratory Data Analysis Report](https://github.com/IstinNew/Cook-Me-Up/blob/main/reports/EDA_report.md)**")
    st.markdown("- 👉 **[Results Analysis Report](https://github.com/IstinNew/Cook-Me-Up/blob/main/reports/results.md)**")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Project updates in progress until January 2025.")