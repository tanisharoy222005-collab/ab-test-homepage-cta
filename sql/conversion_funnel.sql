SELECT
    variant,

    COUNT(DISTINCT session_id) AS visitors,

    COUNT(
        DISTINCT CASE
            WHEN cta_click = 1
            THEN session_id
        END
    ) AS cta_clicks,

    COUNT(
        DISTINCT CASE
            WHEN form_start = 1
            THEN session_id
        END
    ) AS form_starts,

    COUNT(
        DISTINCT CASE
            WHEN conversion = 1
            THEN session_id
        END
    ) AS conversions

FROM experiment_results
GROUP BY variant;
