FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn
RUN playwright install chromium

CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8080"]
