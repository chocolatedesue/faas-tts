from io import BytesIO
# import os
from fastapi import FastAPI
from text import text_to_seq_func, avaliabe_cleaners
from pydantic import BaseModel


from fastapi.responses import StreamingResponse

from typing import List, Union


class g2pBody(BaseModel):
    cleanner_name: str
    # symbols: List[str]
    symbols: Union[List[str], str]
    text: str


class ttsBody(BaseModel):
    sequence: List[int]
    sid: int
    speed: float
    

ort_sess = None
app = FastAPI()

def vits_onnx_infer(seq, speaker_id, speed=1.0,sampling_rate=22050):
    from loguru import logger
    import numpy as np
    import onnxruntime

    global ort_sess
    if not ort_sess:
        from pathlib import Path
        model = Path('./weight/model.onnx')
        # if os.getenv("IS_DOWNLOAD"):
            

        # if not os.path.exists('vits.onnx'):
        if not model.exists():
            raise FileNotFoundError(
                "please provide a model named 'model.onnx' in the ./weight folder.")

        ort_sess = onnxruntime.InferenceSession(str(model))

    x = np.array([seq], dtype=np.int64)
    x_len = np.array([x.shape[1]], dtype=np.int64)
    sid = np.array([speaker_id], dtype=np.int64)
    speed = 1 / speed
    scales = np.array([0.667, speed, 0.8], dtype=np.float32)
    scales.resize(1, 3)
    ort_inputs = {
        'input': x,
        'input_lengths': x_len,
        'scales': scales,
        'sid': sid
    }
    audio = np.squeeze(ort_sess.run(None, ort_inputs))
    audio *= 32767.0 / max(0.01, np.max(np.abs(audio))) * 0.6
    audio = np.clip(audio, -32767.0, 32767.0)
    import pydub
    seg = pydub.AudioSegment(
        audio.astype(np.int16).tobytes(), frame_rate=sampling_rate, sample_width=2, channels=1)
    # return seg
    # seg.export("test.wav", format="wav")
    with BytesIO() as f:
        seg.export(f, format="wav")
        return f.getvalue()





@app.post("/g2p")
def g2p(g2pBody: g2pBody):
    if g2pBody.cleanner_name not in avaliabe_cleaners:
        return {"error": "cleaner_name not found"}
    if isinstance(g2pBody.symbols, str):
        g2pBody.symbols = g2pBody.symbols.replace("[", "")
        g2pBody.symbols = g2pBody.symbols.replace("]", "")
        g2pBody.symbols = g2pBody.symbols.split(",")

    sequence = text_to_seq_func(
        g2pBody.text, [g2pBody.cleanner_name], g2pBody.symbols)
    sequence = str(sequence)
    return {"sequence": sequence}


@app.post("/clean/vits/tts")
def tts(ttsBody: ttsBody):
    # logger.info(ttsBody)
    # return {"success": "success"}
    audio_bytes =  vits_onnx_infer(ttsBody.sequence, ttsBody.sid, ttsBody.speed)
    return StreamingResponse(BytesIO(audio_bytes), media_type="audio/wav")
