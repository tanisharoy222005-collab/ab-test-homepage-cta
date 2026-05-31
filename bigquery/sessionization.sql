SELECT

user_pseudo_id,

ga_session_id,

MIN(event_timestamp) AS session_start,

MAX(event_timestamp) AS session_end

FROM
`project.analytics.events_*`

GROUP BY
user_pseudo_id,
ga_session_id;
