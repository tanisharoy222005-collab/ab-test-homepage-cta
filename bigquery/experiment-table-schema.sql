CREATE TABLE experiment_results (

    event_date DATE,

    user_id STRING,

    session_id STRING,

    variant STRING,

    device_category STRING,

    traffic_source STRING,

    country STRING,

    cta_impression INT64,

    cta_click INT64,

    form_start INT64,

    conversion INT64,

    revenue FLOAT64

);
