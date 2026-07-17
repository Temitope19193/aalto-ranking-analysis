import pandas as pd

# Load your raw data
data = pd.read_csv("Raw Data.csv")

# --- Part 1: What drives the score? (using 2015, same year as your dashboard) ---
data_2015 = data[data["year"] == 2015]

factors = ["quality_of_education", "alumni_employment", "quality_of_faculty",
           "publications", "influence", "citations", "patents"]

correlations = data_2015[factors + ["score"]].corr()["score"].sort_values(ascending=False)

print("=== Correlation of each factor with final score (2015) ===")
print(correlations)
print()

# --- Part 2: Which countries improved the most from 2012 to 2015? ---
avg_by_country_year = data.groupby(["country", "year"])["score"].mean().reset_index()

pivot = avg_by_country_year.pivot(index="country", columns="year", values="score")
pivot["change_2012_to_2015"] = pivot[2015] - pivot[2012]
pivot_sorted = pivot.sort_values("change_2012_to_2015", ascending=False)

print("=== Countries with the biggest score improvement, 2012 to 2015 ===")
print(pivot_sorted[["change_2012_to_2015"]].head(10))