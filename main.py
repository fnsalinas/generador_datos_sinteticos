
from typing import List, Tuple, Dict, Any
from fastapi import FastAPI
import json

from data_generator import get_full_data
from common.config_app import update_config_json

update_config_json()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get_{noclients}_clients")
def read_root(noclients: int):
    clients_list: List[str] = [get_full_data() for i in range(noclients)]
    return json.dumps(clients_list, indent=4)

# URL Documentation for the API: http://localhost:8000/docs
