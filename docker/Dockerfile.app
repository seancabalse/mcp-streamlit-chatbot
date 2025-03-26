# Streamlit app Dockerfile
FROM python:3.10-slim
WORKDIR /app

COPY app /app/app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
