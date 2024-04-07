-- # Write your MySQL query statement below
WITH PreviousWeatherData AS(
    Select id, recordDate, temperature,
    LAG(temperature,1,1000000)
    OVER(ORDER BY recordDate) AS previousDayTemperature,
    LAG(recordDate,1,2100-01-01)
    OVER(ORDER BY recordDate) AS previousDate
    FROM Weather
)
SELECT id 
FROM PreviousWeatherData
where PreviousWeatherData.temperature > PreviousWeatherData.previousDayTemperature
AND recordDate = DATE_ADD(previousDate, INTERVAL 1 DAY)

-- my solution
select w1.Id from Weather w1, Weather w2
where datediff(w1.recordDate, w2.recordDate) =1 AND w1.temperature > w2.temperature;

-- another
SELECT x.id
FROM Weather x
JOIN Weather y ON x.recordDate = y.recordDate + INTERVAL 1 DAY
WHERE x.temperature > y.temperature;