# from io import BytesIO
# import os
# from time import time
# import os
from fastapi import FastAPI, HTTPException
from text import text_to_seq_func, symbols_dict
from app.schemas import CleanTTSBody, G2pBody, g2pResponse,RawTTSBody
from app.vits_onnx import router as vits_onnx_router
from app.g2p import router as g2p_router



ort_sess = None
app = FastAPI()

app.include_router(prefix="/vits_onnx", router= vits_onnx_router)
app.include_router(
    prefix="/g2p",router= g2p_router
)

from os import path

TMP_PATH = "TMP_START_TIME.txt"
if not path.exists(TMP_PATH):
    with open (TMP_PATH,"w") as f:
        from datetime import datetime
        f.write(
            str(datetime.utcnow())
        )



@app.get("/", description="获取部署时间")
def get_start_time():
    with open(TMP_PATH,"r") as f:
        START_TIME = f.read()
        return {"start_time": str(START_TIME),"time_zone":"UTC"}