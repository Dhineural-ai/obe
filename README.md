# OBE Intelligence Platform

## Run Locally

1. Install Python
2. Install requirements

pip install -r requirements.txt

3. Add OpenAI API key in .env

4. Run:

streamlit run app.py

## Deploy on Render

Build Command:
pip install -r requirements.txt

Start Command:
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
