SELECT
    variant,
    COUNT(DISTINCT user_id) AS users_assigned,
    ROUND(
        COUNT(DISTINCT user_id) * 100.0 /
        SUM(COUNT(DISTINCT user_id)) OVER (),
        2
    ) AS allocation_percentage
FROM experiment_results
GROUP BY variant;
