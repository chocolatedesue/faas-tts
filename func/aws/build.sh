

bucket_name=ttslambda
region_name=ap-northeast-1


aws s3api create-bucket --bucket $bucket_name \
--region $region_name \
 --create-bucket-configuration LocationConstraint=$region_name

# aws s3 mb s3://$bucket_name

aws s3 ls s3://$bucket_name

pip install -t ./package -r requirements.txt

# exclude __pycache__ and .git with recursive
7z a -tzip -aoa func.zip app text  handler.py '-xr!__pycache__ -xr!.git'
cd package

7z a -tzip -aoa ../func.zip .

# list files in zip 
7z l func.zip

# force upload
aws s3 cp func.zip s3://$bucket_name/func.zip  


# use s3
aws lambda update-function-code --function-name jpg2p \
--region ap-northeast-1 \
--s3-bucket $bucket_name \
--s3-key func.zip


aws lambda