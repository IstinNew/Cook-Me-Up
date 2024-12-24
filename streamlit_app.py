import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

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

if sections == "Introduction":
    st.header("Introduction")
    st.write("""
    Welcome to the Cook-Me-Up project! This app provides insights into Indian food recipes using Python, Machine Learning, BigQuery, and Looker Studio.
    Navigate through the sections to explore interactive data, visualizations, and insights!
    """)

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

    # Correlation heatmap
    st.subheader("Correlation Heatmap of Preparation and Cooking Times")
    prep_cook_corr = df[['prep_time', 'cook_time']].corr()
    plt.figure(figsize=(6, 4))
    sns.heatmap(prep_cook_corr, annot=True, cmap='coolwarm')
    st.pyplot(plt)

    # Clustering with K-Means
    st.subheader("K-Means Clustering on Cooking and Preparation Times")
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['prep_time', 'cook_time']])
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(df_scaled)
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='prep_time', y='cook_time', hue='cluster', palette='viridis')
    plt.title('Clusters of Cooking and Preparation Times')
    st.pyplot(plt)

    # Integration with Looker Studio
    st.subheader("Looker Studio Integration")
    st.write("Explore enhanced visualizations via Looker Studio:")
    st.markdown("[Click here to view the Looker Studio report](https://example-looker-studio-link.com)")

elif sections == "Insights":
    st.header("Insights")
    st.write("Discover meaningful insights derived from the dataset.")

    # Key takeaways
    st.write("""
    - The majority of dishes are categorized under the 'Others' flavor profile.
    - North and South regions dominate the dataset in terms of the number of dishes.
    - Preparation and cooking times vary significantly, allowing clustering to identify patterns in the data.
    - Visualizations from Looker Studio provide additional depth to the analysis.
    """)
    st.write("More insights will be added as the project progresses!")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Project updates in progress until January 2025.")