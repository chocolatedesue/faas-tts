
pip install -t ./package -r requirements.txt


7z a -tzip -aoa func.zip app text package handler.py

# list files in zip 
7z l func.zip

aws lambda update-function-code --function-name jpg2p \
--region ap-northeast-1 \
--zip-file fileb://./func.zip