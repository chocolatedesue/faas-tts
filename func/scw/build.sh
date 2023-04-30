npm install -g serverless
serverless plugin install -n serverless-scaleway-functions


function build_package(){
#  https://www.scaleway.com/en/docs/serverless/functions/how-to/package-function-dependencies-in-zip/
PYTHON_VERSION=3.10 # or 3.7, 3.8, ...
docker run --rm -v $(pwd):/home/app/function --workdir /home/app/function rg.fr-par.scw.cloud/scwfunctionsruntimes-public/python-dep:$PYTHON_VERSION pip install -r requirements.txt --target ./package
PYTHON_VERSION=3.9 # or 3.7, 3.8, ...
docker run --rm -v $(pwd):/home/app/function --workdir /home/app/function rg.fr-par.scw.cloud/scwfunctionsruntimes-public/python-dep:$PYTHON_VERSION python -m pip install --upgrade pip --no-cache-dir && pip install -r requirements.txt --target ./package --no-cache-dir && cd package && python -c "import pyopenjtalk; pyopenjtalk._lazy_init()" && python -c "import jieba; jieba.initialize()" && cd ..

}

function deplot(){

find . -name "*.pyc" -exec rm -f {} \;
find . -name "__pycache__" -exec rm -rf {} 
sls deploy

}