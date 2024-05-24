from pdfminer.high_level import extract_text
from docx import Document

def extract_questions_from_file(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text(file_path)
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = '\n'.join(para.text for para in doc.paragraphs)
    else:
        raise ValueError("Unsupported file format")
    questions = parse_questions_from_text(text)
    return questions
