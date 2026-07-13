from fpdf import FPDF

# read the report we generated earlier
with open("mis_report.txt", "r", encoding="utf-8") as f:
    report_text = f.read()
    report_text = report_text.encode("latin-1", errors="ignore").decode("latin-1")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

# add each line of the report to the PDF
page_width = pdf.w - 20  # total page width minus margins

for line in report_text.split("\n"):
    pdf.set_x(10)  # always start from the left margin
    if line.strip() == "":
        pdf.ln(8)
    else:
        pdf.multi_cell(page_width, 8, line)

pdf.output("MIS_Report.pdf")
print("Saved MIS_Report.pdf")