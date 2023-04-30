npm install -g serverless
serverless plugin install -n serverless-scaleway-functions


function build_package(){

    # create python3.9
PYTHON_VERSION=3.9 # or 3.7, 3.8, ...
docker run --rm -v $(pwd):/home/app/function --workdir /home/app/function rg.fr-par.scw.cloud/scwfunctionsruntimes-public/python-dep:$PYTHON_VERSION python -m pip install --upgrade pip --no-cache-dir && pip install -r requirements.txt --target ./packages --no-cache-dir

# cd ./packages
# python -c "import pyopenjtalk; pyopenjtalk._lazy_init()"
#   python -c "import jieba; jieba.initialize()"
# cd -

}

function deplot(){

find . -name "*.pyc" -exec rm -f {} \;
find . -name "__pycache__" -exec rm -rf {} 

cd packages
7z a ../func.zip ./* -r
cd ../
7z a func.zip text handlers -r

7z l func.zip

sls deploy --package ./func.zip 

}