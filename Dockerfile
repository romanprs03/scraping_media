FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn
RUN playwright install chromium

CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8000"]
