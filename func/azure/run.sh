

pip install  --target="$PWD/.python_packages/lib/site-packages"  -r requirements.txt

func azure functionapp logstream hkg2p --browser
func azure functionapp publish hkg2p 
func azure functionapp publish hkg2p  --help

func azure functionapp publish hkg2p  --no-build