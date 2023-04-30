FROM public.ecr.aws/lambda/python:3.9

# WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt -t ${LAMBDA_TASK_ROOT} 
RUN    python -c "import pyopenjtalk; pyopenjtalk._lazy_init()" && \
    python -c "import jieba; jieba.initialize()"


COPY  ./handler.py ${LAMBDA_TASK_ROOT}/handler.py
COPY ./app ${LAMBDA_TASK_ROOT}/app
COPY ./text  ${LAMBDA_TASK_ROOT}/text

CMD [ "handler.handler" ]








# FROM public.ecr.aws/lambda/python:3.9

# RUN pip install -U pip && \
#     pip install fastapi mangum uvicorn -t "${LAMBDA_TASK_ROOT}"

# COPY test.py ${LAMBDA_TASK_ROOT}/app.py

# CMD ["app.handler"]
