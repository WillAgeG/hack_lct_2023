FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r /app/requirements.txt --no-cache-dir 

COPY . .

CMD uvicorn predictor.main:app --host 0.0.0.0 --port 8000 --workers 4
