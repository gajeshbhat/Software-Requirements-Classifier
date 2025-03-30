import json
from fpdf import FPDF

def export_to_pdf(data, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for item in data:
        pdf.multi_cell(0, 10, f"Requirement: {item['requirement']}\nClassification: {item['label']}\n\n")

    pdf.output(output_path)
    print(f"✅ PDF saved to {output_path}")

def export_to_json(data, output_path):
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ JSON saved to {output_path}")

def print_to_console(data):
    for i, item in enumerate(data, start=1):
        print(f"[{i}] Requirement: {item['requirement']}")
        print(f"    Classification: {item['label']}")
        print()
