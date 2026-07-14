import sqlite3
import pandas as pd

conn = sqlite3.connect("../output/mis_data.db")

# Query 1: Total sales per category (simple aggregation)
q1 = """
SELECT 
    'M01AB' as category, SUM(M01AB) as total_sales FROM sales
UNION ALL
SELECT 'M01AE', SUM(M01AE) FROM sales
UNION ALL
SELECT 'N02BA', SUM(N02BA) FROM sales
UNION ALL
SELECT 'N02BE', SUM(N02BE) FROM sales
UNION ALL
SELECT 'N05B', SUM(N05B) FROM sales
UNION ALL
SELECT 'N05C', SUM(N05C) FROM sales
UNION ALL
SELECT 'R03', SUM(R03) FROM sales
UNION ALL
SELECT 'R06', SUM(R06) FROM sales
ORDER BY total_sales DESC
"""

print("=== Total sales by category ===")
print(pd.read_sql(q1, conn))

# Query 2: Month-over-month change for one category using a WINDOW FUNCTION
q2 = """
SELECT 
    datum,
    N02BE,
    LAG(N02BE) OVER (ORDER BY datum) as prev_month,
    N02BE - LAG(N02BE) OVER (ORDER BY datum) as change,
    ROUND(
        (N02BE - LAG(N02BE) OVER (ORDER BY datum)) * 100.0 
        / LAG(N02BE) OVER (ORDER BY datum), 2
    ) as pct_change
FROM sales
ORDER BY datum
"""

print("\n=== N02BE month-over-month change ===")
print(pd.read_sql(q2, conn))

conn.close()