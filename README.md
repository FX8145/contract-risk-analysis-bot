# Contract Analysis & Risk Assessment Bot

A GenAI-powered tool that analyzes business contracts, identifies risks,
and explains clauses in simple business English. Built for GUVI x HCL Hackathon.

## 🚀 Features
- Upload PDF, DOCX, or TXT contracts
- Automatic clause extraction
- Named entity extraction (parties, dates, amounts, jurisdiction)
- Clause-by-clause plain-English explanation
- Risk detection (penalty, indemnity, IP transfer, renewal, termination, etc.)
- Contract summary generation
- Hindi → English normalization
- Downloadable audit logs
- Streamlit-based interface

## 🛠 Tech Stack
- Python, Streamlit
- spaCy, NLTK
- GPT-4.1-mini (reasoning only)
- Local JSON logs

## 📁 Project Structure
contract-analysis-bot/
│── app.py
│── requirements.txt
│── README.md
│── outputs/
│── utils/
│── samples/


## ▶ Running Locally

Install dependencies:
pip install -r requirements.txt
python -m spacy download en_core_web_sm


Run the application:
streamlit run app.py