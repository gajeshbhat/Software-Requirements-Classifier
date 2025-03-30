import PyPDF2

def parse_document(path: str) -> str:
    if path.endswith(".txt"):
        with open(path, "r") as f:
            return f.read()
    elif path.endswith(".pdf"):
        text = ""
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    else:
        raise ValueError("Unsupported file format. Use .txt or .pdf")
