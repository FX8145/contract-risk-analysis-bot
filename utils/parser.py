import nltk
nltk.download("punkt")

from nltk.tokenize import sent_tokenize

def extract_clauses(text):
    sentences = sent_tokenize(text)
    return [s.strip() for s in sentences if len(s.strip()) > 5]
