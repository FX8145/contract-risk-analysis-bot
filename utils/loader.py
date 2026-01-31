import docx
import PyPDF2

def read_contract_file(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")

    elif file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    elif "wordprocessingml" in file.type:
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    return ""
