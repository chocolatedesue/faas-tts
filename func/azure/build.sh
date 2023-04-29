

function download_model(){
    mkdir -p ./weight 
    url="https://r2share.ccds.win/vits_onnx/jp/model.onnx"
    config_url="https://r2share.ccds.win/vits_onnx/jp/config.json"

    # url="https://r2share.ccds.win/vits_onnx/jp_cn/model.onnx"
    # config_url="https://r2share.ccds.win/vits_onnx/jp_cn/config.json"

    wget  -O ./weight/model.onnx $url
    wget -O ./weight/config.json $config_url

}


cd .python_packages/lib/site-packages/
python -c "import pyopenjtalk ; pyopenjtalk._lazy_init()"
cd -

func azure functionapp publish $name  --force --python --no-build