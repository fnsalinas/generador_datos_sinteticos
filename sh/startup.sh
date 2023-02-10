#!/bin/bash

# Install Python 3.10 if not installed
if ! command -v python3.10 &> /dev/null
then
    echo "Python 3.10 could not be found"
    echo "Installing Python 3.10"
    sudo apt update && sudo apt upgrade -y;
    sudo apt install software-properties-common -y;
    sudo add-apt-repository ppa:deadsnakes/ppa;
    sudo apt install python3.10 -y;
else
    echo "Python 3.10 already installed"
fi

# Install pip if not installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found"
    echo "Installing pip"
    sudo apt update && sudo apt upgrade -y;
    sudo apt install python3-pip -y;

    sudo apt-get update -y;
    sudo apt install python3-pip -y;
else
    echo "pip already installed"
fi

# Install pipenv if not installed
if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found"
    echo "Installing pipenv"
    sudo apt update && sudo apt upgrade -y;
    sudo apt install python3-pip -y;
    pip install pipenv;
else
    echo "pipenv already installed"
fi

# Install git if not installed
if ! command -v git &> /dev/null
then
    echo "git could not be found"
    echo "Installing git"
    sudo apt update && sudo apt upgrade -y;
    sudo apt install git -y;
else
    echo "git already installed"
fi

# clone the repository https://github.com/fnsalinas/generador_datos_sinteticos.git on main folder if not exists else update it
if [ -d "~/generador_datos_sinteticos" ]; then
    echo "~/generador_datos_sinteticos already exists"
    cd ~/generador_datos_sinteticos/
    git pull;
else
    echo "~/generador_datos_sinteticos does not exist"
    git clone
    cd ~/generador_datos_sinteticos/;


if grep -q "CUSTOM SCRIPTS" ~/.bashrc; then
    echo "CUSTOM SCRIPTS already exists in ~/.bashrc"
else
    echo "CUSTOM SCRIPTS does not exist in ~/.bashrc"
    echo "" >> ~/.bashrc;
    echo "" >> ~/.bashrc;
    echo "" >> ~/.bashrc;
    echo "# ----------- CUSTOM SCRIPTS -----------" >> ~/.bashrc;
    echo "" >> ~/.bashrc;
    echo "" >> ~/.bashrc;
    echo "" >> ~/.bashrc;
    echo "alias python='python3'" >> ~/.bashrc;
fi

source ~/.bashrc;
cd ~/generador_datos_sinteticos/;