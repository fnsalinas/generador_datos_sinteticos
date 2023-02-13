#!/bin/bash

# Install Python 3.10 if not installed
if ! command -v python3.10 &> /dev/null
then
    echo "Python 3.10 could not be found"
    echo "Installing Python 3.10"
    sudo apt update && sudo apt upgrade -y
    sudo apt install software-properties-common -y
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.10 -y
else
    echo "Python 3.10 already installed"
fi

# Install pip if not installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found"
    echo "Installing pip"
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3-pip -y

    sudo apt-get update -y
    sudo apt install python3-pip -y
else
    echo "pip already installed, updating pip"
    sudo apt update && sudo apt upgrade -y
fi

# Install pipenv if not installed
if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found"
    echo "Installing pipenv"
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3-pip -y
    pip install pipenv
else
    echo "pipenv already installed"
fi

# Install git if not installed
if ! command -v git &> /dev/null
then
    echo "git could not be found"
    echo "Installing git"
    sudo apt update && sudo apt upgrade -y
    sudo apt install git -y
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
    git clone https://github.com/fnsalinas/generador_datos_sinteticos.git
    cd ~/generador_datos_sinteticos/
fi


if grep -q "CUSTOM SCRIPTS" ~/.bashrc; then
    echo "CUSTOM SCRIPTS already exists in ~/.bashrc"
else
    echo "CUSTOM SCRIPTS does not exist in ~/.bashrc"
    echo "" >> ~/.bashrc
    echo "" >> ~/.bashrc
    echo "" >> ~/.bashrc
    echo "# ----------- CUSTOM SCRIPTS -----------" >> ~/.bashrc
    echo "" >> ~/.bashrc
    echo "" >> ~/.bashrc
    echo "" >> ~/.bashrc
    echo "alias python='python3'" >> ~/.bashrc
fi

source ~/.bashrc;
cd ~/generador_datos_sinteticos;

# Install dependencies if the actual foldername is generador_datos_sinteticos, if not, exit
if [ "${PWD##*/}" = "generador_datos_sinteticos" ]; then
    echo "Installing dependencies"
    echo "Running pipenv install";
    pipenv install;

    echo "Running pipenv install -r requirements.txt";
    pipenv install -r requirements.txt;

    echo "Running pipenv install -e .";
    pipenv install -e .;
else
    echo "The actual foldername is not generador_datos_sinteticos, exiting"
    exit 1
fi


# install nginx if not installed
if ! command -v nginx &> /dev/null
then
    echo "nginx could not be found"
    echo "Installing nginx"
    sudo apt update && sudo apt upgrade -y
    sudo apt install nginx -y
    
    echo "Configuring nginx"
    sudo ufw app list
    sudo ufw allow 'Nginx HTTP'
    
    echo writing nginx config
    sudo echo "server {
        listen 80;
        server_name 52.14.11.142;
        location / {
            proxy_pass http://127.0.0.1:8000;
        }
    }" > /etc/nginx/sites-enabled/fastapi_nginx
    sudo service nginx restart
else
    echo "nginx already installed"
fi
