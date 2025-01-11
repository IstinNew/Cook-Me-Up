-- SQL script for initial exploratory data analysis using BigQuery
-- Get the distribution of flavor profiles by course
SELECT course, flavor_profile, COUNT(*) AS count
FROM `RecipeInsightsDB.IndianFood_Sorted`
GROUP BY course, flavor_profile;