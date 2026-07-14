import pandas as pd
import sqlite3

# load the CSV
df = pd.read_csv("../data/salesmonthly.csv")

# create (or connect to) a database file called mis_data.db
conn = sqlite3.connect("../output/mis_data.db")

# save the dataframe as a table called 'sales' inside that database
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Done! Data loaded into mis_data.db as table 'sales'")

# quick check: read it back and print first 5 rows
check = pd.read_sql("SELECT * FROM sales LIMIT 5", conn)
print(check)

conn.close()