#!/bin/bash

cd ~;
APPPATH=$(find . -print | grep -i 'generador_datos_sinteticos$')

cd $APPPATH;

pipenv run uvicorn main:app --reload;

# save the result of the command in a variable find . -print | grep -i 'generador_datos_sinteticos$'



