import pandas as pd

daily = pd.read_csv("salesdaily.csv")
daily["datum"] = pd.to_datetime(daily["datum"])
print("Last 5 dates in daily data:")
print(daily["datum"].tail(5))
print("\nVery last date:", daily["datum"].max())