🧾 Contract Analysis & Risk Assessment Bot

AI-powered multilingual contract analyzer built using GPT-5.2, capable of identifying risks, extracting entities, and summarizing obligations/rights in simple business language.

🚀 Features

✔ Detects contract language (English / Tamil / More)

✔ Identifies key legal risks (Termination, Jurisdiction, Auto-renewal, Penalty, IP Transfer…)

✔ Extracts entities (Parties, Dates, Amounts, Jurisdiction)

✔ Extracts Obligations / Rights / Prohibitions

✔ Generates clean, readable summaries

✔ Modern Streamlit interface

✔ Supports .txt contracts


🛠 Installation
1️⃣ Clone Repository
git clone https://github.com/FX8145/contract-risk-analysis-bot.git
cd contract-risk-analysis-bot

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your API Key

Create .env file:

OPENAI_API_KEY=your_key_here

▶️ Run the Project
streamlit run app.py

📌 Output Includes

Detected contract language

Detailed paragraph-based risk analysis

Multilingual NER with clear descriptions

Obligations, Rights & Prohibitions in simple English

💡 Tech Stack

Python

Streamlit

OpenAI GPT-5.2


spaCy / NLTK

