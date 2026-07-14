import sys
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from google import genai
import datetime

import os
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

top3 = pd.read_csv("../output/top3_kpis.csv")
kpi_text = top3.to_string(index=False)


prompt = f"""You are an automated MIS writing assistant. Your output MUST strictly follow this Markdown structure. Do not include any introductory text like "Here is your report."

📈 Top KPI Shifts

For each row below, write one line: [Category] changed by [pct_change]% - [one-sentence plain-English reason based on the reason column].

Data:
{kpi_text}
"""

response = client.models.generate_content(
  model="gemini-flash-latest",
    contents=prompt
)

summary_text = response.text

footer = f"""

---
Generated from: salesmonthly.csv (last complete month used)
Generated on: {datetime.datetime.now().strftime('%d %b %Y, %I:%M %p')}
KPIs analyzed: {len(top3)}
Status: Human Review Required
"""

final_report = summary_text + footer
print(final_report)

with open("../output/mis_report.txt", "w", encoding="utf-8") as f:
    f.write(final_report)