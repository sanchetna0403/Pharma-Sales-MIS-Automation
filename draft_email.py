import os

with open("mis_report.txt", "r", encoding="utf-8") as f:
    report_text = f.read()

# .eml is a universal email file format - opens in Outlook, Gmail desktop, etc.
# as an editable draft, without ever sending anything.
eml_content = f"""Subject: MIS Report - AI Generated (Pending Review)
Content-Type: text/plain; charset="utf-8"

{report_text}
"""

with open("MIS_Report_Draft.eml", "w", encoding="utf-8") as f:
    f.write(eml_content)

print("Draft email file created: MIS_Report_Draft.eml")
print("Open this file to review before manually sending.")