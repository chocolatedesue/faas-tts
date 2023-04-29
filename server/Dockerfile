FROM python:3.9.16-slim-buster

WORKDIR /app

COPY  requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -c "import pyopenjtalk; pyopenjtalk._lazy_init()" && \
    python -c "import jieba; jieba.initialize()"

COPY /app /app/app/
COPY text/ /app/text/


EXPOSE 8000
CMD ["uvicorn", "app:app", "--port", "8000" , "--host", "0.0.0.0" ]