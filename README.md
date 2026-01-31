AI-powered multilingual contract analyzer built using GPT-5.2, capable of identifying risks, extracting entities, and summarizing obligations/rights in simple business language.

🚀 Features

✔ Detects contract language (English / Tamil / More)

✔ Identifies key legal risks (Termination, Jurisdiction, Auto-renewal, Penalty, IP Transfer…)

✔ Extracts entities (Parties, Dates, Amounts, Jurisdiction)

✔ Extracts Obligations / Rights / Prohibitions

✔ Generates clean, readable summaries

✔ Modern Streamlit interface

✔ Supports .txt contracts

📂 Project Structure
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
