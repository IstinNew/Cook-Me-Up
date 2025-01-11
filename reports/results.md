
# **Analysis Results**  
**Cook-Me-Up Project: Simplifying Culinary Delights with Data**  

---

## **Key Findings**  

### **1. Diet Preferences**  
- **Vegetarian Dominance**: 78% of the dishes are vegetarian.  
- **Non-Vegetarian Dishes**: Comprise 22%, primarily from coastal regions.  

---

### **2. Regional Highlights**  

| Region        | Most Used Ingredient | Unique Ingredients Count |  
|---------------|-----------------------|---------------------------|  
| North India   | Ghee                 | 25                        |  
| South India   | Coconut              | 20                        |  
| East India    | Mustard Oil          | 15                        |  
| West India    | Jaggery              | 10                        |  

---

### **3. Fastest Dishes**  
The top 3 dishes with the shortest preparation times:  

| Dish Name           | Total Time (mins) |  
|---------------------|--------------------|  
| Poha               | 10                 |  
| Upma               | 12                 |  
| Chutney            | 15                 |  

---

### **4. Flavor Profile Insights**  

| Flavor Profile | Most Common Course | Count |  
|----------------|--------------------|-------|  
| Spicy          | Main Course        | 120   |  
| Sweet          | Dessert            | 80    |  
| Bitter         | Appetizer          | 10    |  

---

## **5. Pair Plot Insights**  

### **Understanding the Pair Plot**  
The pair plot explores relationships between key features of the Indian Food 101 dataset. Features visualized include:  

1. **Total Time**: Combined preparation and cooking time.  
2. **Number of Ingredients**: Total count of ingredients per recipe.  
3. **Flavor Profile**: Categorization of dish flavors (e.g., spicy, sweet, savory).  
4. **Course**: Type of dish (appetizer, main course, dessert).  
5. **Region**: Geographical origin of the recipe.  

### **Key Observations**  
- **Diagonal KDE Plots**:  
  - **Total Time**: Most recipes have shorter cooking times, with a highly skewed distribution.  
  - **Number of Ingredients**: The peak occurs around 6 ingredients, the most common count.  
- **Off-Diagonal Scatter Plots**:  
  - **Total Time vs. Number of Ingredients**: Recipes with fewer ingredients tend to have shorter cooking times, though some outliers exist.  
  - **Flavor Profile vs. Course**: Distinct relationships between desserts and sweet flavors are evident.  
  - **Regional Trends**: Differences in cooking styles and ingredients across regions.  

### **Insights Derived**  
- **Regional Variations**: Highlights differences in cooking styles, ingredients, and preparation times across regions.  
- **Complex Recipes**: Identifies outliers in total time, representing more elaborate dishes.  
- **Course Patterns**: Distinct clustering of appetizers, main courses, and desserts based on flavor and complexity.  

👉 **[View the Pair Plot](../images/Pair_Plot.png)**  

This pair plot aids in understanding patterns for recipe categorization, optimization, and regional diversity.  

---

## **SQL Analysis Highlights**  

- **Average Cooking Time by Region**:  
  - **North**: 40 mins  
  - **South**: 35 mins  
  - **East**: 45 mins  
  - **West**: 30 mins  

- **Top Ingredients by Region**:  
  - Ghee, Coconut, Mustard Oil, Jaggery  

---

## **Clustering Insights**  

Recipes were grouped into three clusters using unsupervised machine learning:  

1. **Quick Recipes**: Less than 20 minutes.  
2. **Moderate Recipes**: Between 20–45 minutes.  
3. **Long Recipes**: More than 45 minutes.  

---

## **Conclusion**  

This analysis highlights the diversity in Indian cuisine, including variations in flavor, diet preferences, and preparation styles. These insights lay the foundation for further machine learning integration, interactive user recommendations, and recipe optimization.

---
