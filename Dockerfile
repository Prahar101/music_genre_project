FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
EXPOSE 8501

ENV NAME World
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8080 & streamlit run front.py --server.port 8501 --server.address 0.0.0.0"]
