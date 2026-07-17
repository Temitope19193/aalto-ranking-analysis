# University Ranking Analysis — SQL, Python & Power BI

A self-directed data project built to demonstrate the data mining, analysis and 
reporting skills described in the Aalto EE Data Analyst/Engineer job posting.

## What this project does

Using a public world university rankings dataset (2012–2015), this project:

- **Structures the data** into a relational database using **SQL** (SQLite) — 
  filtering, sorting and aggregating to surface ranking patterns
- **Analyses statistically** in **Python** (pandas) — testing which ranking 
  criteria most strongly predict a university's overall score and tracking 
  country-level trends over time
- **Visualises** the findings in an interactive **Power BI** dashboard

## Key findings

1. **Faculty quality** is the strongest predictor of overall ranking score 
   (correlation 0.71) stronger than research output or alumni employment.
2. **Quality beats scale** — Singapore and Israel outperform the USA and UK 
   on average score despite having far fewer ranked universities.
3. **The Netherlands, Denmark and Norway** show the strongest upward momentum 
   in average score from 2012 to 2015.

Full write-up: see `Ranking_Insight_Summary.pdf`

## Files in this repo

| File | Description |
|------|-------------|
| `Raw Data.csv` | Original dataset |
| `sql_queries.txt` | SQL queries used for filtering, sorting, and aggregation |
| `analyze_rankings.py` | Python script generating the top-10 countries chart |
| `correlation_analysis.py` | Python script for correlation and trend analysis |
| `country_scores.csv` | SQL query output used in Python and Power BI |
| `top10_countries_chart.png` | Chart output from Python |
| `power_bi_dashboard.pdf` | Exported Power BI dashboard |
| `Ranking_Insight_Summary.pdf` | One-page written summary of findings |

## Tools used

SQL (SQLite) · Python (pandas) · Power BI

---
Built by [Temitope Sodola] as part of an application to Aalto University Executive 
Education's AI and Digitalization team.
