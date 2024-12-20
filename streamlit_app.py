import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Define the absolute path to the dataset
csv_file_path = r"D:\WBS Coding\Bootcamp\Project Works\Final Project\Working\Streamlit\indian_food.csv"

# Function to load the dataset
@st.cache_data
def load_data(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data.fillna('Unknown', inplace=True)
    
    # Remove duplicates
    data.drop_duplicates(inplace=True)
    
    # Replace invalid values
    data['flavor_profile'] = data['flavor_profile'].replace('-1', 'Others')
    data['state'] = data['state'].replace('-1', 'Others')
    data['region'] = data['region'].replace('-1', 'Others')
    data['cook_time'] = data['cook_time'].replace(-1, 0)
    data['prep_time'] = data['prep_time'].replace(-1, 0)
    return data

# Load data
df = load_data(csv_file_path)

# Create a sorted copy of the dataframe
df_sorted = df.copy()

# Replace -1 values with 'Others' in df_sorted
df_sorted['flavor_profile'] = df_sorted['flavor_profile'].replace('-1', 'Others')
df_sorted['state'] = df_sorted['state'].replace('-1', 'Others')
df_sorted['region'] = df_sorted['region'].replace('-1', 'Others')
df_sorted['cook_time'] = df_sorted['cook_time'].replace(-1, 0)
df_sorted['prep_time'] = df_sorted['prep_time'].replace(-1, 0)

# Streamlit app layout
st.title("Cook-Me-Up: Indian Food Insights")
st.sidebar.title("Navigation")

# Sidebar navigation
sections = st.sidebar.radio("Sections", ["Introduction", "Data Overview", "Visualizations", "Insights"])

if sections == "Introduction":
    st.header("Introduction")
    st.write("""
    Welcome to the Cook-Me-Up project! Explore a comprehensive dataset of Indian food recipes.
    Navigate through the sections to discover data insights, visualizations, and more!
    """)

elif sections == "Data Overview":
    st.header("Data Overview")
    st.write("Here is a preview of the dataset:")
    st.dataframe(df_sorted.head())

    st.write("Summary statistics:")
    st.write(df_sorted.describe())

    # Display unique values
    st.write("Unique values in 'flavor_profile':", df_sorted['flavor_profile'].unique())
    st.write("Unique values in 'state':", df_sorted['state'].unique())
    st.write("Unique values in 'region':", df_sorted['region'].unique())
    st.write("Unique values in 'cook_time':", df_sorted['cook_time'].unique())
    st.write("Unique values in 'prep_time':", df_sorted['prep_time'].unique())
    st.write("Unique values in 'course':", df_sorted['course'].unique())
    st.write("Unique values in 'diet':", df_sorted['diet'].unique())

    # Course distribution per region
    course_distribution = df_sorted.groupby('region')['course'].value_counts().unstack().fillna(0)

    plt.figure(figsize=(12, 8))
    sns.heatmap(course_distribution, annot=True, cmap='coolwarm')
    plt.title('Course Distribution per Region')
    plt.xlabel('Course')
    plt.ylabel('Region')
    st.pyplot(plt)

elif sections == "Visualizations":
    st.header("Visualizations")
    st.write("Explore the dataset through the following visualizations.")

    # Create empty lists for each region's ingredients
    InEast, InWest, InNorth, InOthers, InNorthEast, InSouth, InCentral = ([] for _ in range(7))

    # Fill the lists with ingredients based on the region
    for row in range(len(df_sorted)):
        region = df_sorted['region'][row]
        ingredients = df_sorted['ingredients'][row].split(', ')
        if region == 'East':
            InEast.extend(ingredients)
        elif region == 'West':
            InWest.extend(ingredients)
        elif region == 'North':
            InNorth.extend(ingredients)
        elif region == 'North East':
            InNorthEast.extend(ingredients)
        elif region == 'South':
            InSouth.extend(ingredients)
        elif region == 'Central':
            InCentral.extend(ingredients)
        else:
            InOthers.extend(ingredients)

    # Create a series with all unique ingredients
    all_ingredient = pd.Series(InEast + InWest + InNorth + InOthers + InNorthEast + InSouth + InCentral).unique()

    # Count occurrences of each ingredient in the respective lists
    InEastCount = [InEast.count(ingredient) for ingredient in all_ingredient]
    InWestCount = [InWest.count(ingredient) for ingredient in all_ingredient]
    InNorthCount = [InNorth.count(ingredient) for ingredient in all_ingredient]
    InOthersCount = [InOthers.count(ingredient) for ingredient in all_ingredient]
    InNorthECount = [InNorthEast.count(ingredient) for ingredient in all_ingredient]
    InSouthCount = [InSouth.count(ingredient) for ingredient in all_ingredient]
    InCentralCount = [InCentral.count(ingredient) for ingredient in all_ingredient]

    # Create a DataFrame with the counts for each region
    ingredient_per_region = pd.DataFrame({
        'East': InEastCount, 'West': InWestCount, 'North': InNorthCount, 'Others': InOthersCount,
        'North East': InNorthECount, 'South': InSouthCount, 'Central': InCentralCount
    }, index=all_ingredient)

    # Add a column for the total count
    ingredient_per_region['Sum'] = ingredient_per_region.sum(axis=1)

    # Plot the heatmap of ingredient correlations
    plt.figure(figsize=(14, 10), dpi=100)
    correlation_matrix = ingredient_per_region.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Heatmap of Ingredient Correlations Across Regions')
    st.pyplot(plt)

elif sections == "Insights":
    st.header("Insights")
    st.write("""
    Key takeaways:
    - Most dishes fall under the 'Others' flavor profile.
    - Preparation and cooking times vary significantly across dishes.
    """)
    st.write("Exploring more insights as work continues on the project!")

st.sidebar.markdown("---")
st.sidebar.info("Project updates in progress until January 2025.")