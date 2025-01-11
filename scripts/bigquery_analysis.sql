-- SQL script for more in-depth analysis, meaningful insights using BigQuery
-- Get the distribution of flavor profiles by course
SELECT course, flavor_profile, COUNT(*) AS count
FROM `RecipeInsightsDB.IndianFood_Sorted`
GROUP BY course, flavor_profile;

-- Get the top 10 ingredients used in dishes from each region
SELECT region, ingredients, COUNT(*) AS count
FROM `RecipeInsightsDB.IndianFood_Sorted`
GROUP BY region, ingredients
ORDER BY region, count DESC
LIMIT 10;

-- Calculate the total preparation and cooking time for each dish and get the top 10 fastest dishes
SELECT name, prep_time + cook_time AS total_time
FROM `RecipeInsightsDB.IndianFood_Sorted`
ORDER BY total_time ASC
LIMIT 10;

-- Get a count of dishes by diet type
SELECT diet, COUNT(*) AS count
FROM `RecipeInsightsDB.IndianFood_Sorted`
GROUP BY diet;

-- Get the average preparation and cooking time by region
SELECT region, AVG(prep_time) AS avg_prep_time, AVG(cook_time) AS avg_cook_time
FROM `RecipeInsightsDB.IndianFood_Sorted`
GROUP BY region;

-- Get the number of unique ingredients used in each region
SELECT region, COUNT(DISTINCT ingredients) AS unique_ingredients
FROM `RecipeInsightsDB.IndianFood_Sorted`
GROUP BY region;