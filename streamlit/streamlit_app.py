import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the path to the dataset in the streamlit folder
file_path = "streamlit/indian_food.csv"

# Function to load the dataset
@st.cache
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
data = load_data(file_path)

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
    st.dataframe(data.head())

    st.write("Summary statistics:")
    st.write(data.describe())

elif sections == "Visualizations":
    st.header("Visualizations")
    st.write("Explore the dataset through the following visualizations.")

    # Flavor Profile Distribution
    st.subheader("Flavor Profile Distribution")
    flavor_counts = data['flavor_profile'].value_counts()
    fig, ax = plt.subplots()
    flavor_counts.plot(kind='bar', color='skyblue', ax=ax)
    plt.title("Flavor Profile Distribution")
    plt.xlabel("Flavor Profile")
    plt.ylabel("Count")
    st.pyplot(fig)

    # Cook Time vs Prep Time
    st.subheader("Cook Time vs Prep Time")
    fig, ax = plt.subplots()
    sns.scatterplot(x='prep_time', y='cook_time', data=data, ax=ax)
    plt.title("Cook Time vs Prep Time")
    plt.xlabel("Preparation Time (mins)")
    plt.ylabel("Cooking Time (mins)")
    st.pyplot(fig)

elif sections == "Insights":
    st.header("Insights")
    st.write("""
    Key takeaways:
    - Most dishes fall under the 'Others' flavor profile.
    - Preparation and cooking times vary significantly across dishes.
    """)

    st.write("Explore more insights as you continue working on the project!")

st.sidebar.markdown("---")
st.sidebar.info("Project updates in progress until January 2025.")