
from typing import List, Tuple, Dict, Any
from fastapi import FastAPI
import json

from data_generator import get_full_data

app = FastAPI()

@app.get("/")
def read_root():
    FULL_DATA: Dict[str, Any] = get_full_data()
    return json.dumps(FULL_DATA, indent=4)