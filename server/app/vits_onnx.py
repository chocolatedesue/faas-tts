from fastapi import HTTPException
from app.schemas import CleanTTSBody, RawTTSBody
from io import BytesIO
from text import text_to_seq_func, symbols_dict
from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter
from app.util import download_with_tqdm

router = APIRouter(
    tags=["vits_onnx"]
)

ort_sess = None 


def vits_onnx_infer(ttsBody: CleanTTSBody):
    seq, speaker_id, speed, noise, noisew, sampling_rate = ttsBody.sequence, ttsBody.sid, ttsBody.lenth, ttsBody.noise, ttsBody.noisew, ttsBody.sample_rate

    from loguru import logger
    import numpy as np
    import onnxruntime
    from pathlib import Path

    global ort_sess
    model = Path('./weight/model.onnx')
    if not ort_sess:
        
        
        # if os.getenv("IS_DOWNLOAD"):
        if not model.parent.exists():
            model.parent.mkdir(parents=True)

        if not model.exists():
          
            import os 
            from loguru import logger 
            url = None
            config_url = None
            if os.getenv("MODEL_URL") and os.getenv("CONFIG_URL"):
                logger.info("Downloading model from MODEL_URL")
                url = os.getenv("MODEL_URL")
                config_url = os.getenv("CONFIG_URL")
                # download_with_tqdm(url, str(model))


            elif os.getenv("IS_DOWNLOAD_JP_MODEL"):
    
                logger.info("Downloading jp model from r2share.ccds.win")
                url = "https://r2share.ccds.win/vits_onnx/jp/model.onnx"
                config_url = "https://r2share.ccds.win/vits_onnx/jp/config.json"
                
                # download_with_tqdm(url, str(model))

            elif os.getenv("IS_DOWNLOAD_JP_CN_MODEL"):
                logger.info("Downloading jp_cn model from r2share.ccds.win")
                url = "https://r2share.ccds.win/vits_onnx/jp_cn/model.onnx"
                # download_with_tqdm(url, str(model))
                config_url = "https://r2share.ccds.win/vits_onnx/jp_cn/config.json"

            # if not os.path.exists('vits.onnx'):
            else:
                raise HTTPException(status_code=500, detail="Model not found, please set MODEL_URL or IS_DOWNLOAD_JP_MODEL or IS_DOWNLOAD_JP_CN_MODEL or put model.onnx in ./weight/")
            # if url and config_url:
            # try:
            download_with_tqdm(url, str(model))
            download_with_tqdm(config_url, str(model.parent / "config.json"))
            

 

    ort_sess = onnxruntime.InferenceSession(str(model))

    x = np.array([seq], dtype=np.int64)
    x_len = np.array([x.shape[1]], dtype=np.int64)
    sid = np.array([speaker_id], dtype=np.int64)
    speed = 1 / speed
    scales = np.array([noise, speed, noisew], dtype=np.float32)
    scales.resize(1, 3)
    ort_inputs = {
        'input': x,
        'input_lengths': x_len,
        'scales': scales,
        'sid': sid
    }
    try:
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
    except Exception as e:
        logger.error(e)
        e_msg = str(e)
        raise HTTPException(status_code=500, detail=f"""
            possible error: sid bigger than expected
            model.onnx error: {e_msg}
        """)
    

@router.post("/clean/tts",response_class=StreamingResponse)
def clean_tts(ttsBody: CleanTTSBody):

    if isinstance(ttsBody.sequence, str):
        ttsBody.sequence = ttsBody.sequence.replace("[", "")
        ttsBody.sequence = ttsBody.sequence.replace("]", "")
        ttsBody.sequence = ttsBody.sequence.split(",")
        ttsBody.sequence = [int(i) for i in ttsBody.sequence]

    audio_bytes =  vits_onnx_infer(ttsBody)
    return StreamingResponse(BytesIO(audio_bytes), media_type="audio/wav")


@router.post("/raw/tts",response_class=StreamingResponse)
def raw_tts(ttsBody: RawTTSBody):
    clean_text, seq = text_to_seq_func(
        ttsBody.g2pConfig.text, [ttsBody.g2pConfig.cleanner_name], ttsBody.g2pConfig.symbols)
    ttsBody = CleanTTSBody(sid=ttsBody.sid, lenth=ttsBody.lenth, noise=ttsBody.noise,
                            noisew=ttsBody.noisew, sample_rate=ttsBody.sample_rate, sequence=seq)
    audio_bytes =  vits_onnx_infer(ttsBody)
    return StreamingResponse(BytesIO(audio_bytes), media_type="audio/wav")


@router.get("/model_config")
def get_model_config():
    from pathlib import Path
    import json
    model_config = Path('./weight/config.json')
    if not model_config.exists():
        raise HTTPException(status_code=500, detail="config.json not found, please put config.json in ./weight/")

    with open(model_config, "r") as f:
        config = json.load(f)
    return config