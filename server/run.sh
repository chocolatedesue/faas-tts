# export IS_DOWNLOAD_JP_MODEL &&  uvicorn app:app --reload 
# export IS_DOWNLOAD_JP_CN_MODEL &&  uvicorn app:app --reload
#  docker run -p 8000:8000 --rm --name test 

function docker {
    docker build . -t test 
    docker run -p 8000:8000 --rm --name test \
    -e IS_DOWNLOAD_JP_CN_MODEL=foo \
    -v $(pwd)/weight:/app/weight \
    test
}

function add_env {
    export PATH=$PATH:~/.local/bin
}

# mkdir -p  ../func/azure/app
# rm -rf  ../func/azure/app 
rsync ./app ../func/azure -avzh  --exclude '__pycache__' --dry-run
rsync ./text ../func/azure -avzh --exclude '__pycache__'    --dry-run



rsync ./app ../func/azure -avzh  --exclude '__pycache__'
rsync ./text ../func/azure -avzh --exclude '__pycache__'

rsync ./app ../func/aws -azvh  --exclude '__pycache__'
rsync ./text ../func/aws -azvh --exclude '__pycache__'