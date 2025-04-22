import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

skill_keywords = ["Python", "Java", "Flask", "Machine Learning", "Data Analysis", "Django", "SQL", "React", "NLP"]

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    doc = nlp(text)
    skills_found = [token.text for token in doc if token.text in skill_keywords]
    return list(set(skills_found))

