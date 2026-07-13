import pandas as pd

# change 'your_file.csv' to the exact filename you see in the sidebar
df = pd.read_csv("salesmonthly.csv")

print("Shape (rows, columns):", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values per column:")
print(df.isnull().sum())