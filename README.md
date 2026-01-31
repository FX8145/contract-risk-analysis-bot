🧾 Contract Analysis & Risk Assessment Bot

AI-powered multilingual contract analyzer built using GPT-5.2, capable of detecting risks, extracting entities, and summarizing obligations/rights in simple language.

🚀 Features

✔ Detects contract language (English / Tamil / More)
✔ Identifies legal risks (Termination, Jurisdiction, Auto-renewal, Penalty, IP Transfer, etc.)
✔ Extracts entities (Parties, Dates, Amounts, Jurisdiction)
✔ Extracts obligations, rights & prohibitions
✔ Readable and business-friendly summaries
✔ Modern Streamlit UI
✔ Supports .txt contracts

📂 Project Structure (Short Diagram)
contract-risk-bot/
│── app.py
│── requirements.txt
│── README.md
│── .env
│
├── utils/
│   ├── llm_reasoner.py
│   ├── multilingual_extractor.py
│   ├── multilingual_obligations.py
│   ├── multilingual_risk_detector.py
│   ├── loader.py
│   └── parser.py
│
├── samples/
│   ├── sample_contract - English.txt
│   └── sample_contract - Tamil.txt
│
└── outputs/
    └── results.json

🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/contract-risk-bot.git
cd contract-risk-bot

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Add Your API Key

Create .env file:

OPENAI_API_KEY=your_key_here

▶️ Run the App
streamlit run app.py

📊 Output Screenshots (as shown in project)

✔ Language detected (English/Tamil)

✔ Full paragraph-based risk analysis

✔ Entity extraction in natural readable format

✔ Obligations, Rights & Prohibitions in clear summaries

💡 Tech Stack

Python

Streamlit (Modern UI)

OpenAI GPT-5.2

spaCy + Regex (fallback)

NLTK

🏁 Final Notes

This project fully satisfies the GUVI Hackathon problem statement by delivering:
✔ Multilingual support
✔ Clause-by-clause insights
✔ Risk analysis reports
✔ Business-friendly explanations
✔ Ready for legal teams / SMEs
