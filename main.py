
from typing import List, Tuple, Dict, Any
from fastapi import FastAPI
import json

from data_generator import get_full_data
from common.config_app import update_config_json

config: Dict[str, Any] = update_config_json()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_{noclients}_clients")
def read_root(noclients: int):
    if noclients > 100:
        return {"Error": "The number of clients must be less than 100, use the endpoint /get_100_clients_csv to get a csv file with more than 100 clients"}
    clients_list: List[str] = [get_full_data() for i in range(noclients)]
    return json.dumps(clients_list)

@app.get("/get_{noclients}_clients_csv")
def read_root(noclients: int):
    if noclients > 100:
        return {"Error": "The number of clients must be less than 100, use the endpoint /get_100_clients_csv to get a csv file with more than 100 clients"}
    clients_list: List[str] = [get_full_data() for i in range(noclients)]
    return json.dumps(clients_list)

# URL Documentation for the API: http://localhost:8000/docs


if __name__ == "__main__":
    import uvicorn
    print("-"*10 + f"IP identificada: {config['ip']}:{config['port']}" + "-"*10)
    uvicorn.run(app, host=config["ip"], port=config["port"])
