import pdfplumber

def extract_text_from_pdf(file):
    try:
        text = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

        return text.strip()

    except Exception as e:
        print("PDF parsing error:", e)
        return ""
