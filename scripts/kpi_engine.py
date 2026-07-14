import sqlite3
import pandas as pd

conn = sqlite3.connect("../output/mis_data.db")
df = pd.read_sql("SELECT * FROM sales", conn)
conn.close()

# make sure dates are sorted properly
df["datum"] = pd.to_datetime(df["datum"])
df = df.sort_values("datum")
df = df.iloc[:-1]  # drop the last row - it's an incomplete month


categories = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
print(df.tail(5)[["datum"] + categories])

# get the latest month and the one before it
latest = df.iloc[-1]
previous = df.iloc[-2]

results = []
for cat in categories:
    curr_val = latest[cat]
    prev_val = previous[cat]
    pct_change = round((curr_val - prev_val) / prev_val * 100, 2)

    # simple rule-based reasoning
    if abs(pct_change) < 5:
        reason = "Stable - normal fluctuation"
    elif pct_change >= 5:
        reason = "Notable increase - check demand/promo activity"
    else:
        reason = "Notable decrease - check supply or demand drop"

    results.append({
        "category": cat,
        "current_value": curr_val,
        "previous_value": prev_val,
        "pct_change": pct_change,
        "reason": reason
    })

kpi_df = pd.DataFrame(results)

# sort by absolute % change, biggest movers first
kpi_df["abs_change"] = kpi_df["pct_change"].abs()
kpi_df = kpi_df.sort_values("abs_change", ascending=False)

print("=== All categories, ranked by change magnitude ===")
print(kpi_df[["category", "current_value", "previous_value", "pct_change", "reason"]])

print("\n=== TOP 3 movers ===")
top3 = kpi_df.head(3)
print(top3[["category", "pct_change", "reason"]])

# save this for the next step (AI layer)
top3.to_csv("../output/top3_kpis.csv", index=False)
print("\nSaved top3_kpis.csv for next step")