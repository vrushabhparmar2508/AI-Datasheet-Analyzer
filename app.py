import streamlit as st
import pdfplumber
import google.generativeai as genai

# --- 🛑 STOP AND PASTE YOUR NEW API KEY HERE 🛑 ---
# Generate a NEW key from Google AI Studio and put it here:
MY_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Tell the Google library to use your key
genai.configure(api_key=MY_API_KEY)

# We are using Gemini 1.5 Pro because it is the best at reading long documents
# FIX: Removed the extra dash at the end of the model name!
model = genai.GenerativeModel('gemini-2.5-flash')

# --- Web App Layout ---
st.set_page_config(page_title="EC Datasheet Analyzer", layout="wide")
st.title("⚡ EC Datasheet Analyzer & C-Header Generator")
st.write("Upload a microcontroller datasheet to automatically extract specs and generate a .h file!")

uploaded_file = st.file_uploader("Upload PDF Datasheet here", type="pdf")

if uploaded_file is not None:
    st.success("File uploaded successfully! Extracting text... ⏳")
    
    try:
        # 1. Read the PDF File
        extracted_text = ""
        # Using pdfplumber to open the uploaded file
        with pdfplumber.open(uploaded_file) as pdf:
            # For this test, let's just read the first 5 pages so it's fast!
            for page in pdf.pages[:5]: 
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
                    
        st.info("Text extracted! Sending to AI for analysis. Please wait a few seconds... 🧠")

        # 2. The AI Prompt (The Magic Instructions)
        prompt = f"""
        You are an expert embedded software engineer. I am giving you text extracted from a microcontroller datasheet.
        
        Please do the following:
        1. Give a brief summary of what this component is.
        2. Extract key specifications (Operating Voltage, Max Current, Communication interfaces like I2C/SPI).
        3. Generate a clean, well-commented C-language Header (.h) file containing useful macros and pin definitions based on the text.
        
        Here is the Datasheet Text:
        {extracted_text}
        """

        # 3. Send to Gemini and get the response
        response = model.generate_content(prompt)

        # 4. Display the results on the website!
        st.subheader("🤖 AI Analysis Results:")
        st.markdown(response.text)
        
        st.balloons() # Let's celebrate a successful run!
        
        # 5. Provide a Download Button
        st.download_button(
            label="📥 Download C-Header (.h) File",
            data=response.text,
            file_name="config.h",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Oops! Something went wrong: {e}")