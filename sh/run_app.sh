#!/bin/bash

cd ~;
APPPATH=$(find . -print | grep -i 'generador_datos_sinteticos$')

echo "-----------> APPPATH:" $APPPATH;
cd $APPPATH;

# pipenv run uvicorn main:app --reload;
pipenv run python main.py;
# save the result of the command in a variable find . -print | grep -i 'generador_datos_sinteticos$'



