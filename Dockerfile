# Base image: chhota Linux + Python 3.12
FROM python:3.12-slim

# Container ke andar /app folder mein kaam karo
WORKDIR /app

# Pehle sirf requirements copy karke install karo (cache ka fayda)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Phir baaki code copy karo
COPY . .

# App port 8000 pe chalega
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]