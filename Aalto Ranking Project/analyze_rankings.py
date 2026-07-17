import pandas as pd
import matplotlib.pyplot as plt

# Load the data we exported from SQL
data = pd.read_csv("country_scores.csv")

# Look at just the top 10 countries
top10 = data.head(10)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top10["country"], top10["average_score"], color="steelblue")
plt.xlabel("Country")
plt.ylabel("Average Score") 
plt.title("Top 10 Countries by Average University Ranking Score (2015)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as an image
plt.savefig("top10_countries_chart.png")
plt.show()

print("Chart created successfully!")