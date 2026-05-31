# Tracking Plan

| Event Name | Trigger | Parameters |
|------------|----------|------------|
| experiment_view | Variant Assigned | variant_name |
| cta_impression | CTA Visible | variant_name |
| cta_click | CTA Clicked | variant_name |
| lead_form_start | Form Interaction | variant_name |
| lead_form_submit | Successful Submission | variant_name |

## GA4 Custom Dimensions

variant_name

### Possible Values

- control
- variant_b

## Validation Process

- GTM Preview Mode
- GA4 DebugView
- BigQuery Export Validation
