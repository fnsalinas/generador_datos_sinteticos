#!/bin/bash

cd ~;
APPPATH=$(ls -lsrtah ~/ | grep -i generador_datos_sinteticos$);
APPPATH=$(echo $APPPATH | awk '{print $NF}' | tail -1);

echo "-----------> APPPATH:" $APPPATH;
cd $APPPATH;

# pipenv run uvicorn main:app --reload;
cd /home/ubuntu/workspace/fsalinas/generador_datos_sinteticos/;
pipenv run python src/push_data_to_postgresql.py;
# save the result of the command in a variable find . -print | grep -i 'generador_datos_sinteticos$'



