FROM python:3.9.16-bullseye

WORKDIR /app

COPY  requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt 

COPY app /app/app

CMD ["uvicorn", "app:app", "--port", "8000"]