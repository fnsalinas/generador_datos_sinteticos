
from typing import List, Tuple, Dict, Any
from fastapi import FastAPI
import json

from data_generator import FULL_DATA

app = FastAPI()

@app.get("/")
def read_root():
    return json.dumps(FULL_DATA, indent=4)