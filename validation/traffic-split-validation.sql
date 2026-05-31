SELECT
    variant,

    COUNT(DISTINCT user_id) AS users,

    ROUND(
        COUNT(DISTINCT user_id) * 100.0 /
        SUM(COUNT(DISTINCT user_id)) OVER (),
        2
    ) AS traffic_share

FROM experiment_results

GROUP BY variant;
