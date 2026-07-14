import sqlite3
import pandas as pd

conn = sqlite3.connect("../output/mis_data.db")
df = pd.read_sql("SELECT * FROM sales", conn)
conn.close()

df.to_csv("../output/sales_for_excel.csv", index=False)
print("Exported sales_for_excel.csv")