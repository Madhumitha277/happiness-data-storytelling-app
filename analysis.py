import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("cleaned_2015.csv")

# 🔍 Clean column names properly
data.columns = data.columns.str.strip()
data.columns = data.columns.str.replace(" ", "_")
data.columns = data.columns.str.replace("(", "", regex=False)
data.columns = data.columns.str.replace(")", "", regex=False)

# Print columns to verify
print("Columns:", data.columns)

# ✅ Try to find correct GDP column automatically
gdp_col = None
for col in data.columns:
    if "gdp" in col.lower():
        gdp_col = col

# ✅ Try to find happiness column automatically
happiness_col = None
for col in data.columns:
    if "happiness" in col.lower() or "score" in col.lower():
        happiness_col = col

print("Using GDP column:", gdp_col)
print("Using Happiness column:", happiness_col)

# ❌ If still not found → stop
if gdp_col is None or happiness_col is None:
    print("Column not found. Check dataset.")
    exit()

# 📊 Top 10 chart
top10 = data.sort_values(by=happiness_col, ascending=False).head(10)

plt.figure()
plt.bar(top10['Country'], top10[happiness_col])
plt.xticks(rotation=45)
plt.title("Top 10 Happiest Countries")
plt.savefig("top10.png")
plt.close()

# 📊 GDP vs Happiness
plt.figure()
plt.scatter(data[gdp_col], data[happiness_col])
plt.xlabel("GDP")
plt.ylabel("Happiness")
plt.title("GDP vs Happiness")
plt.savefig("gdp_vs_happiness.png")
plt.close()

print("Charts created successfully!")