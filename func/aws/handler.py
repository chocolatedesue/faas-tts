from mangum import Mangum
from app import app 


handler = Mangum(app, lifespan="off")

# dir(handler)
if __name__ == "__main__":
    import os
    from pathlib import Path
    model_path = Path("./weight/model.onnx")
    if not model_path.parent.exists():
        model_path.parent.mkdir(parents=True)
    config_path = Path("./weight/config.json")
    if not config_path.parent.exists():
        config_path.parent.mkdir(parents=True)

    if os.getenv("MODEL_URL") and os.getenv("CONFIG_URL"):
        from app.util import download_with_tqdm
        url = os.getenv("MODEL_URL")
        config_url = os.getenv("CONFIG_URL")
        download_with_tqdm(url, str(model_path))
        download_with_tqdm(config_url, str(config_path))
    

    elif os.getenv("IS_DOWNLOAD_JP_MODEL"):
        from app.util import download_with_tqdm
        url = "https://r2share.ccds.win/vits_onnx/jp/model.onnx"
        config_url = "https://r2share.ccds.win/vits_onnx/jp/config.json"
        download_with_tqdm(url, str(model_path))
        download_with_tqdm(config_url, str(config_path))
    elif os.getenv("IS_DOWNLOAD_JP_CN_MODEL"):
        from app.util import download_with_tqdm
        url = "https://r2share.ccds.win/vits_onnx/jp_cn/model.onnx"
        config_url = "https://r2share.ccds.win/vits_onnx/jp_cn/config.json"
        download_with_tqdm(url, str(model_path))
        download_with_tqdm(config_url, str(config_path))
    


    import uvicorn
    uvicorn.run(
        app, host='0.0.0.0',port=8000
    )