WITH experiment_summary AS (
    SELECT
        variant,
        COUNT(DISTINCT session_id) AS sessions,
        SUM(cta_click) AS clicks,
        SUM(conversion) AS conversions
    FROM experiment_results
    GROUP BY variant
)

SELECT
    variant,
    sessions,
    clicks,
    conversions,
    ROUND((clicks * 100.0 / sessions), 2) AS ctr_percent,
    ROUND((conversions * 100.0 / sessions), 2) AS conversion_rate_percent
FROM experiment_summary
ORDER BY variant;
