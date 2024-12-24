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

# Streamlit app layout
st.title("Cook-Me-Up: Indian Food Insights")
st.sidebar.title("Navigation")

# Sidebar navigation
sections = st.sidebar.radio("Sections", ["Introduction", "Interactive Data Overview", "Visualizations", "Insights"])

# WordCloud function
def create_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    st.pyplot(plt)

if sections == "Introduction":
    st.header("Introduction")
    st.write("""
    Welcome to the Cook-Me-Up project! This app provides insights into Indian food recipes using Python, Machine Learning, BigQuery, and Looker Studio.
    Navigate through the sections to explore interactive data, visualizations, and insights!
    """)

    # Create word cloud for recipes requiring advance prep
    final_data = df  # Assuming the dataset is prepared as `final_data`
    
    # Filter titles based on advance prep required (ensure this column exists in the data)
    advance_prep_titles = ' '.join(final_data[final_data['advance prep required']]['title'])
    no_advance_prep_titles = ' '.join(final_data[~final_data['advance prep required']]['title'])

    # Generate and display the word clouds
    create_wordcloud(advance_prep_titles, 'Common Words in Titles of Recipes Requiring Advance Prep')
    create_wordcloud(no_advance_prep_titles, 'Common Words in Titles of Recipes Not Requiring Advance Prep')

elif sections == "Interactive Data Overview":
    st.header("Interactive Data Overview")
    st.write("Explore the dataset interactively using filters.")

    # Filter options
    selected_flavor = st.selectbox("Select Flavor Profile", options=df['flavor_profile'].unique())
    selected_region = st.multiselect("Select Region(s)", options=df['region'].unique(), default=df['region'].unique())
    selected_diet = st.radio("Select Diet", options=df['diet'].unique())

    # Filter dataset
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

    # Region selection for ingredient frequency visualization
    region_selection = st.selectbox('Select Region to Display Ingredient Frequency', df['region'].unique())

    # Create lists for ingredients per region
    InEast, InWest, InNorth, InOthers, InNorthEast, InSouth, InCentral = [], [], [], [], [], [], []
    for row in range(len(df)):
        if df['region'][row] == 'East':
            InEast.extend(df['ingredients'][row].split(', '))
        elif df['region'][row] == 'West':
            InWest.extend(df['ingredients'][row].split(', '))
        elif df['region'][row] == 'North':
            InNorth.extend(df['ingredients'][row].split(', '))
        elif df['region'][row] == 'North East':
            InNorthEast.extend(df['ingredients'][row].split(', '))
        elif df['region'][row] == 'South':
            InSouth.extend(df['ingredients'][row].split(', '))
        elif df['region'][row] == 'Central':
            InCentral.extend(df['ingredients'][row].split(', '))
        else:
            InOthers.extend(df['ingredients'][row].split(', '))

    # Count ingredients in each region
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

    # Creating DataFrame for ingredient counts per region
    ingredient_per_region = pd.DataFrame(ingredient_counts, index=all_ingredient)
    ingredient_per_region['Sum'] = ingredient_per_region.sum(axis=1)

    # Section 1: Top 15 Ingredients in the selected region
    st.subheader(f'Top 15 Ingredients in {region_selection} Region')
    ord_region = ingredient_per_region.sort_values([region_selection], ascending=False)[0:15]
    plt.figure(figsize=(12, 8), dpi=100)
    sns.barplot(x=ord_region[region_selection], y=ord_region.index, palette='Paired')
    plt.xlabel('Count')
    plt.ylabel('Ingredients')
    plt.title(f'{region_selection} Ingredient Frequency')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Section 2: Pairplot for Prep Time, Cook Time, and Diet
    st.subheader("Pairplot of Preparation Time, Cooking Time, and Diet")
    plt.figure(figsize=(10, 8))
    sns.pairplot(df[['prep_time', 'cook_time', 'diet']], hue='diet', palette='Set1')
    st.pyplot(plt)

    # Section 3: Integration with Looker Studio
    st.subheader("Looker Studio Integration")
    st.write("Explore enhanced visualizations via Looker Studio:")
    st.markdown("[Click here to view the Looker Studio report](https://example-looker-studio-link.com)")

elif sections == "Insights":
    st.header("Insights")
    st.write("Discover meaningful insights derived from the dataset.")

    # Key takeaways
    st.write("""
    - North and South regions dominate the dataset in terms of the number of dishes.
    - Preparation and cooking times vary significantly, allowing clustering to identify patterns in the data.
    - Visualizations from Looker Studio provide additional depth to the analysis.
    """)
    st.write("More insights will be added as the project progresses!")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Project updates in progress until January 2025.")