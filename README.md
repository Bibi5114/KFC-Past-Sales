# KFC-Past-Sales
Analysis KFC-Past-Sales datas
**Dataset:** [KFC Global Sales Dataset (2018–2024)](https://www.kaggle.com/datasets/usman44m/kfc-global-sales-dataset-20182024)
## Dataset and Purpose

We use a Kaggle dataset with **8,000 records, 7 columns, 5 countries, and 13 branch IDs**, covering **2018–2024**. It includes year, month, country, branch, sales, customers, and marketing spending. Each row is a branch-related sales record, but some branches have multiple records in the same month. The Kaggle description does not confirm whether the data is real or synthetic.

Our dashboard is for a **regional operations manager**, who reviews branch performance **every Monday**. **If the manager sees a branch with declining sales performance, they will contact the branch manager and investigate.**

Without the dashboard, comparing spreadsheets from different branches would take more time and could make problems easier to miss. A dashboard is better than a fixed weekly report because the manager can filter by country, branch, and year to investigate different questions.

## Dashboard Design

We chose **three headline metrics**: average sales per record, average customers per record, and sales per customer. They give a quick picture of performance.

We added **two charts**: a monthly average sales trend to show when performance changes, and a branch comparison chart to show where performance differs. The **country, branch, and year filters** help the manager focus on relevant results.

The KPIs appear at the **top** for a quick overview, followed by the **charts** for explanation, with **data notes at the bottom**.

We decided **not to show**:
- All 8,000 raw rows, because they would crowd the page.
- A separate marketing-spending chart, because our main decision is about branch sales performance.

**Data limitations:** Some branches have multiple records in the same month, so the charts use **average sales per record**, not verified monthly branch totals. The currency is unspecified, and the dataset is a historical snapshot rather than live data. Cross-country sales comparisons also need caution.

## Refresh and Action

In a real business, data would **refresh nightly**, while the manager would **review it every Monday**. Real-time updates are unnecessary for a weekly management decision.

We would track **weekly branch sales** and investigate a drop of **more than 15%** from the previous week. This is a proposed threshold, not one validated by the dataset. The current CSV cannot calculate weekly changes or send alerts because it does not contain daily data.

If the data is a day or a week out of date, the manager could miss a sales problem and delay action.

**Data shown:** 2018–2024 Kaggle snapshot | **Intended production refresh:** Daily
