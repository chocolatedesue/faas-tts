
code ~/.config/scw/config.yaml
code %USERPROFILE%/.config/scw/config.yaml


scw function runtime list

# create python3.9
PYTHON_VERSION=3.9 # or 3.7, 3.8, ...
docker run --rm -v $(pwd):/home/app/function --workdir /home/app/function rg.fr-par.scw.cloud/scwfunctionsruntimes-public/python-dep:$PYTHON_VERSION pip install -r requirements.txt --target ./package

scw function namespace list

scw function function create -h

scw function function create \
namespace-id=9e4b0808-39df-4d67-850b-a3765a18a008 \
name=frg2pjp runtime=python39 \
min-scale=0 \
handler=handler.handler 