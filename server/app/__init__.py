from io import BytesIO
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

