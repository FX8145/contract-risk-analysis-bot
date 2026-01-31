import streamlit as st
from utils.llm_reasoner import (
    detect_language,
    multilingual_ner,
    extract_obligations_rights,
    detect_risks
)

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("🧾 Contract Analysis & Risk Assessment Bot")

uploaded = st.file_uploader("Upload contract file (.txt, .pdf, .docx)", type=["txt"])

if uploaded:
    text = uploaded.read().decode("utf-8", errors="ignore")

    st.header("🔍 Detected Language")
    lang = detect_language(text)
    st.success(f"Detected Language: **{lang}**")

    st.header("🛑 Identified Risks")
    risks = detect_risks(text, lang)
    st.markdown(risks, unsafe_allow_html=True)

    st.header("📑 Entities (Multilingual NER)")
    ents = multilingual_ner(text, lang)
    st.markdown(ents, unsafe_allow_html=True)

    st.header("⚖️ Obligations / Rights / Prohibitions")
    ob = extract_obligations_rights(text, lang)
    st.markdown(ob, unsafe_allow_html=True)
