function clean_cache(){
    # remove all __pycache__ in current directory and subdirectory
    find . -name '__pycache__' -type d -exec rm -rf {} +
    
}

function test(){
    docker push 985441773004.dkr.ecr.ap-northeast-1.amazonaws.com/vits_onnx:test
    
    docker run --rm -p 9000:8080   985441773004.dkr.ecr.ap-northeast-1.amazonaws.com/vits_onnx:latest
    
    curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
    
}

function test2(){
    docker build . -t test
    docker run --rm -p 9000:8080 test
    
    docker run --rm -p 9000:8080   -e IS_DOWNLOAD_JP_MODEL=1 test
}

function download_jp_model(){
    url="https://r2share.ccds.win/vits_onnx/jp/model.onnx"
    config_url="https://r2share.ccds.win/vits_onnx/jp/config.json"
    mkdir -p ./weight
    wget -O ./weight/model.onnx $url
    wget -O ./weight/config.json  $config_url
    
    
}