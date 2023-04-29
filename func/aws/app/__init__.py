# from io import BytesIO
# import os
# from time import time
# import os
from fastapi import FastAPI, HTTPException
from text import text_to_seq_func, symbols_dict
from app.schemas import CleanTTSBody, G2pBody, g2pResponse,RawTTSBody
from app.vits_onnx import router as vits_onnx_router
from app.g2p import router as g2p_router
from app.test import router as test_router




ort_sess = None
app = FastAPI()

app.include_router(prefix="/vits_onnx", router= vits_onnx_router)
app.include_router(
    prefix="/g2p",router= g2p_router
)
app.router.include_router(
    prefix="/test",router= test_router
)

from os import path

TMP_PATH = "TMP_START_TIME.txt"
if not path.exists(TMP_PATH):
    with open (TMP_PATH,"w") as f:
        from datetime import datetime
        utc_now = datetime.utcnow()
        timestamp = utc_now.timestamp()
        f.write(
            f"timestamp {timestamp} UTC {utc_now.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        # f.write(
        #     f"  {timestamp} UTC {utc_now.strftime('%Y-%m-%d %H:%M:%S')}"
        # )



@app.get("/", description="获取部署时间")
def get_start_time():
    with open(TMP_PATH,"r") as f:
        START_TIME = f.read()
        return {"start_time": str(START_TIME)}