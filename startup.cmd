echo "123456"
uvicorn main:app --host 0.0.0.0 --port 80 &
streamlit run front.py
