-- Which city has the lowest average price?
SELECT city  FROM Listings group by city order by avg(price) asc limit 1

-- want to see the average price as well
SELECT 
    city, 
    AVG(price) AS average_price
FROM 
    Listings
GROUP BY 
    city
ORDER BY 
    average_price ASC
LIMIT 1;
