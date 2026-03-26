# ⚡ AI-Powered EC Datasheet Analyzer & C-Header Generator

## 📖 Overview
In embedded systems development, engineers often spend hours parsing through highly unstructured, 100+ page component datasheets just to locate critical electrical parameters (operating voltages, I2C/SPI addresses, maximum current ratings) and map pinouts. 

This project is an AI-driven web application designed to automate that workflow. By uploading a PDF datasheet, the application uses Natural Language Processing (NLP) to extract key engineering specifications and automatically generates a syntactically correct, ready-to-use C-language Header (`.h`) file for microcontroller integration.

## ✨ Key Features
* **Automated PDF Parsing:** Extracts raw text and tables from complex component datasheets.
* **Intelligent Extraction:** Utilizes Large Language Models to identify and isolate core electrical limits and communication protocols, filtering out marketing jargon.
* **Dynamic Code Generation:** Automatically writes well-commented C-code macros and pin definitions based on the extracted data.
* **Interactive UI:** A clean, user-friendly frontend built for quick drag-and-drop workflow.

## 🛠️ Tech Stack
* **Language:** Python
* **Frontend:** Streamlit
* **AI Model:** Google Gemini 1.5 Pro API
* **Libraries:** pdfplumber, google-generativeai

## 🚀 How to Run Locally
1. Clone this repository.
2. Install the required packages: `pip install streamlit pdfplumber google-generativeai`
3. Add your Gemini API key to the `app.py` file.
4. Run the app: `python -m streamlit run app.py`
