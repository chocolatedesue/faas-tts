function clean_cache(){
    # remove all __pycache__ in current directory and subdirectory
    find . -name '__pycache__' -type d -exec rm -rf {} +
    
}

function test{
    docker push 985441773004.dkr.ecr.ap-northeast-1.amazonaws.com/vits_onnx:test

    docker run --rm -p 9000:8000   985441773004.dkr.ecr.ap-northeast-1.amazonaws.com/vits_onnx:latest

    curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
    
}