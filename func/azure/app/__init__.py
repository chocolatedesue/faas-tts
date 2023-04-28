from fastapi import FastAPI
from text import text_to_seq_func, avaliabe_cleaners
from pydantic import BaseModel

from typing import List,Union


class g2pBody(BaseModel):
    cleanner_name: str
    symbols: Union[str, List[str]]
    text: str


app = FastAPI()


@app.post("/g2p")
async def g2p(g2pBody: g2pBody):
    if g2pBody.cleanner_name not in avaliabe_cleaners:
        return {"error": "cleaner_name not found"}
    
    if isinstance(g2pBody.symbols, str):
        g2pBody.symbols = g2pBody.symbols.replace("[", "")
        g2pBody.symbols = g2pBody.symbols.replace("]", "")
        g2pBody.symbols = g2pBody.symbols.split(",")
        g2pBody.symbols = [g2pBody.symbols]

    sequence = text_to_seq_func(
        g2pBody.text, [g2pBody.cleanner_name], g2pBody.symbols)
    # sequence = str(sequence)
    return {"sequence": sequence}


