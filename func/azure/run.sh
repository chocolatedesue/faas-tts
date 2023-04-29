

# func azure function list-functions 
# az functionapp list 
az functionapp list --query "[].{name:name,resourceGroup:resourceGroup}" -o table

name=jpg2p
group_name=$name"_group"
storage_name=$name"_storage"
region=eastasia

az group create --name $group_name --location $region

az storage account create --name $storage_name --resource-group $group_name --location eastasia --sku Standard_LRS

az functionapp create --name $name --resource-group $group_name \
--consumption-plan-location $region --os-type Linux \
--runtime python --runtime-version 3.9 --functions-version 4 \
--disable-app-insights true \
--storage-account  $storage_name 


az functionapp config appsettings set --name $name --resource-group $group_name \
--setting  IS_DOWNLOAD_JP_MODEL=1

az functionapp config appsettings  delete --name $name --resource-group $group_name \
--setting  IS_DOWNLOAD_JP_MODEL

func azure functionapp publish $name  --force --python   --build-native-deps
func azure functionapp publish $name  --force --python --no-build

# get log stream from azure
func azure functionapp logstream $name 