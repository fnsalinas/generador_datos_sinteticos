#!/bin/bash

cd ~/generador_datos_sinteticos/;
pipenv run uvicorn main:app --reload;


