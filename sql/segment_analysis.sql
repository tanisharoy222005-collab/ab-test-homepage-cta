SELECT
    device_category,
    variant,

    COUNT(*) AS sessions,

    SUM(conversion) AS conversions,

    ROUND(
        SUM(conversion) * 100.0 /
        COUNT(*),
        2
    ) AS conversion_rate

FROM experiment_results

GROUP BY
    device_category,
    variant

ORDER BY
    device_category,
    variant;
