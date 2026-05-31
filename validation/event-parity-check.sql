SELECT
    variant,

    SUM(cta_impression) AS impressions,

    SUM(cta_click) AS clicks,

    SUM(form_start) AS form_starts,

    SUM(conversion) AS conversions

FROM experiment_results

GROUP BY variant;
