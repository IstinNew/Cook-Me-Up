-- SQL script for generating visualizations and input to Looker Studio
-- For exploring the Indian Food dataset
SELECT 
  region,
  state,
  flavor_profile,
  diet,
  COUNT(name) AS dish_count,
  AVG(prep_time + cook_time) AS avg_total_time,
  AVG(ARRAY_LENGTH(SPLIT(ingredients, ','))) AS avg_ingredients_count
FROM 
  `RecipeInsightsDB.IndianFood_Sorted`
GROUP BY 
  region, state, flavor_profile, diet
ORDER BY 
  dish_count DESC;