FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=120 -r requirements.txt
RUN opentelemetry-bootstrap -a install

COPY app.py .

EXPOSE 5000

CMD ["opentelemetry-instrument", "--traces_exporter", "otlp", "--metrics_exporter", "otlp", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
