# export IS_DOWNLOAD_JP_MODEL &&  uvicorn app:app --reload 
# export IS_DOWNLOAD_JP_CN_MODEL &&  uvicorn app:app --reload
#  docker run -p 8000:8000 --rm --name test 

function docker {
    docker build . -t test 
    docker run -p 9000:8000 --rm --name test \
    -e IS_DOWNLOAD_JP_MODEL=foo \
    test
}

# mkdir -p  ../func/azure/app
# rm -rf  ../func/azure/app 
rsync ./app ../func/azure/app -avzh --dry-run --exclude '__pycache__' 
rsync ./text ../func/azure/text -avzh --dry-run --exclude '__pycache__'

rsync ./app ../func/azure/app -avzh  --exclude '__pycache__'
rsync ./text ../func/azure/text -avzh --exclude '__pycache__'

rsync ./app ../func/scw/handlers/app -avzh --dry-run --exclude '__pycache__'
rsync ./text ../func/scw/handlers/text -avzh --dry-run --exclude '__pycache__'

rsync ./app ../func/scw/handlers/app -avzh  --exclude '__pycache__'
rsync ./text ../func/scw/handlers/text -avzh --exclude '__pycache__'