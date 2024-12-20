## Getting Started

Follow these instructions to set up the project locally on your machine.

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Cook-Me-Up.git
   cd Cook-Me-Up

2. **Create a Virtual Environment**
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. **Install Dependencies**
   Install all the required libraries by using requirements.txt:
   ```
   pip install -r requirements.txt

4. **Data Acquisition**

   4.1 Download [Indian Food 101](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101)  
    Save the dataset as a CSV file.
   
   4.2 Import the Dataset into BigQuery
    Log in to your Google Cloud Console.
    Navigate to BigQuery.
    Create a new dataset and table, then upload the CSV file.

5. **Run the Streamlit App Locally**
    After setting up the virtual environment and installing the dependencies, you can run the Streamlit app locally:
   ```
    streamlit run streamlit/streamlit_app.py
   ```
   This will start the app locally at http://localhost:8501, where you can explore the Indian food dataset interactively.

6. **Deploy the App on Streamlit Cloud**

   Create an account on Streamlit Cloud.

   Link your GitHub repository to Streamlit Cloud.

   Deploy the app by selecting the repository and specifying the streamlit/streamlit_app.py script.

   The app will be available at the link provided by Streamlit Cloud, for example: https://cook-me-up.streamlit.app/.

7. **Data Cleaning**
   Run the data cleaning script to prepare the dataset for analysis.
```
   python scripts/data_cleaning.py
```

8. **Exploratory Data Analysis, Data Engineering**
8.1 Explore the Dataset
8.2 Perform initial exploratory data analysis (EDA) to understand the data.
8.3 Extract relevant features for analysis and machine learning models.

9. **Machine Learning**
   Implement clustering algorithms to categorize recipes.
```
   python scripts/machine_learning.py
```

10. **Visualization**
10.1 Connect Looker Studio to BigQuery
10.2 Open Looker Studio.
10.3 Connect to your BigQuery dataset.
10.4 Create Dashboards
10.5 Develop interactive dashboards for data visualization.
   
11. **Contact**
For any questions or issues, please contact [istinnew.github@gmail.com].
