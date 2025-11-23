FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

RUN pip install gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]