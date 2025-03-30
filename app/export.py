from fpdf import FPDF

def export_to_pdf(data, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for item in data:
        pdf.multi_cell(0, 10, f"Requirement: {item['requirement']}\nClassification: {item['label']}\n\n")

    pdf.output(output_path)
