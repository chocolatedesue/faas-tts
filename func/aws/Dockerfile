FROM public.ecr.aws/lambda/python:3.9

# WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -c "import pyopenjtalk; pyopenjtalk._lazy_init()" && \
    python -c "import jieba; jieba.initialize()"


COPY  ./handler.py ${LAMBDA_TASK_ROOT}/handler.py
COPY ./app ${LAMBDA_TASK_ROOT}/app
COPY ./text  ${LAMBDA_TASK_ROOT}/text

CMD [ "handler.handler" ]









