SELECT
    event_date,
    COUNT(*) AS sessions
FROM experiment_results
GROUP BY event_date
ORDER BY event_date;
