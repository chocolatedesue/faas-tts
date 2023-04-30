from typing import List, Union
from pydantic import BaseModel


class G2pBody(BaseModel):
    cleanner_name: str
    # symbols: List[str]
    symbols: Union[List[str], str]
    text: str

class DefaultG2pBody(BaseModel):
    text:str 



class g2pResponse(BaseModel):
    sequence: List[int]
    clean_text: str


class BaseTTSBody(BaseModel):
    '''
       sid: 说话人ID，由所使用的模型决定
       speed: 调节语音长度，相当于调节语速，该数值越大语速越慢。
       lenth: 噪声
       noisew: 噪声偏差
    '''
    # noise(可用于控制感情等变化程度) lenth(可用于控制整体语速) noisew(控制音素发音长度变化程度) sample_rate(采样率, 取决于训练模型的采样率)
    # sequence: Union[List[int], str]
    sid: int
    lenth: float = 1.0
    noise: float = 0.667
    noisew: float = 0.8
    sample_rate: int = 22050


class RawTTSBody(BaseTTSBody):
    g2pConfig: G2pBody


class CleanTTSBody(BaseTTSBody):
    sequence: Union[List[int], str]
    

    