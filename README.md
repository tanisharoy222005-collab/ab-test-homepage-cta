# Homepage CTA A/B Test

## Overview

This project demonstrates an end-to-end A/B testing workflow for optimizing homepage CTA performance using GA4, GTM, SQL, and Python.

The goal was to determine whether changing CTA messaging could improve lead generation performance.

## Business Problem

Homepage visitors were engaging with content but converting into leads below target expectations.

Current CTA:

Request Demo

Proposed CTA:

Book Free Consultation

## Hypothesis

Changing CTA messaging to emphasize consultation value will increase lead form submissions.

## Experiment Design

- Traffic Split: 50/50
- Duration: 14 Days
- Audience: New Visitors
- Primary KPI: Lead Conversion Rate
- Secondary KPI: CTA Click Through Rate
- Confidence Level: 95%

## Results

| Metric | Control | Variant B |
|----------|----------|----------|
| CTA CTR | 6.2% | 7.1% |
| Conversion Rate | 4.1% | 4.6% |
| Relative Lift | - | +12.2% |

## Recommendation

Deploy Variant B to all eligible traffic.

## Repository Structure

- Experiment Design
- Tracking Plan
- GTM Configuration
- SQL Analysis
- Statistical Validation
- Dashboard Reporting
