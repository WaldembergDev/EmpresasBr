FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Substitua a última linha do seu arquivo por esta:
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]