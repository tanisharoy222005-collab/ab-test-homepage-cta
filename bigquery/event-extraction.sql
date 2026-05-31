SELECT

event_date,

user_pseudo_id AS user_id,

event_name,

(SELECT value.string_value
FROM UNNEST(event_params)
WHERE key = 'variant_name')
AS variant

FROM
`project.analytics.events_*`

WHERE
event_name IN (
'cta_click',
'lead_form_submit'
);
