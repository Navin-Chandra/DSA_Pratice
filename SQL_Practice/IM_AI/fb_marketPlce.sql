-- Question
-- Can you find the average price of items listed in each category on Facebook Marketplace? We want to understand the pricing trends across different categories.

-- -- Tables
-- Explore data
-- Listings(listing_id, category, price, city, user_id)
SELECT category , avg(price) FROM Listings group by category;
