from app.schemas import CleanTTSBody, RawTTSBody
from io import BytesIO
from text import text_to_seq_func, symbols_dict
from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter

router = APIRouter(
    tags=["vits_onnx"]
)



def vits_onnx_infer(ttsBody: CleanTTSBody):
    seq, speaker_id, speed, noise, noisew, sampling_rate = ttsBody.sequence, ttsBody.sid, ttsBody.lenth, ttsBody.noise, ttsBody.noisew, ttsBody.sample_rate

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
    scales = np.array([noise, speed, noisew], dtype=np.float32)
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