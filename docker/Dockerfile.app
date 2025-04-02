# Streamlit app Dockerfile
FROM python:3.11-slim
WORKDIR /app

# Install required packages
COPY pyproject.toml .
RUN pip install --upgrade pip && \
    pip install -e .

# Copy the application code
COPY app /app/app

CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
