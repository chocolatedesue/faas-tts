from fastapi import HTTPException
from app.schemas import G2pBody, g2pResponse
from text import text_to_seq_func, symbols_dict
from fastapi import APIRouter

router = APIRouter(
    tags=["g2p"]
)


@router.post("/{cleaner_name}", response_model=g2pResponse)
def jp2_g2p(
    text:str ,
    cleaner_name:str
):
    avaliabe_cleaners = list(symbols_dict.keys())
    if cleaner_name not in avaliabe_cleaners:
        raise HTTPException(status_code=404, detail=f"cleaner_name {cleaner_name} not found, avaliabe_cleaners: {str(avaliabe_cleaners)}")
    
    

    clean_text, sequence = text_to_seq_func(
        text, [cleaner_name], symbols_dict[cleaner_name]
    )
    
    return {"sequence": sequence, "clean_text": clean_text}





@router.post("/", response_model=g2pResponse)
def g2p(g2pBody: G2pBody):

    avaliabe_cleaners = list(symbols_dict.keys())
    if g2pBody.cleanner_name not in avaliabe_cleaners:
        return {"error": "cleaner_name not found"}
    if isinstance(g2pBody.symbols, str):
        g2pBody.symbols = g2pBody.symbols.replace("[", "")
        g2pBody.symbols = g2pBody.symbols.replace("]", "")
        g2pBody.symbols = g2pBody.symbols.split(",")

    clean_text, sequence = text_to_seq_func(
        g2pBody.text, [g2pBody.cleanner_name], g2pBody.symbols)
    
    return {"sequence": sequence, "clean_text": clean_text}


@router.get(
    "/",description="get avaliable cleaners and symbols"
)
def get_symbols_dict():
    # return {"avaiable_cleaners": list(symbols_dict.keys())}
    return {"avaiable_cleaners": symbols_dict}