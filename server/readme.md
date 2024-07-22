## Installation of FastAPI

#### Install venv

```pwsh
python -m venv .venv
```
This will install your virtual environment so you dont gloablly install packages. 

```pwsh
./.venv/Scripts/activate
```
This will start your virtual environment

#### Install Packages with pip 

```pwsh
pip install fastapi uvicorn

pip install fastapi-cors
```
This installs our api framework and hosting service. 

#### Running our API

```pwsh
python main.py
```
Runs the server at the localhost port defined in uvicorn instance. (generally `http://127.0.0.1:8000`)

#### Closing Server
```pwsh
deactivate
```
This closes your venv. If not it will run forever. 

