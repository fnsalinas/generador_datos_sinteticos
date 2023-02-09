#!/bin/bash

# Guarda la fecha/hora en una variable
fecha=$(date +"%Y-%m-%d %H:%M:%S")

cd ~/workspace/fsalinas/generador_datos_sinteticos

git status;
git add .;
git commit -m "Actualización de datos $fecha";
git push;
