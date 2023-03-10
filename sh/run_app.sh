#!/bin/bash

cd ~/workspace/;
APPPATH=$(ls -lsrtah ~/workspace/ | grep -i generador_datos_sinteticos$);
APPPATH=$(echo $APPPATH | awk '{print $NF}' | tail -1);

echo "-----------> APPPATH:" $APPPATH;
cd $APPPATH;

# pipenv run uvicorn main:app --reload;
pipenv run python main.py;
# save the result of the command in a variable find . -print | grep -i 'generador_datos_sinteticos$'



