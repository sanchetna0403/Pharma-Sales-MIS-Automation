import subprocess

scripts = [
    "load_to_db.py",
    "kpi_engine.py",
    "ai_summary.py",
    "export_pdf.py",
    "draft_email.py"
]

for script in scripts:
    print(f"\n=== Running {script} ===")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR in {script}:")
        print(result.stderr)
        break  # stop the pipeline if something fails