#!/bin/bash
# check if the mysql server is installed
# if not, install it
if ! [ -x "$(command -v mysql)" ]; then
    echo 'Error: mysql is not installed.' >&2
    # download deb file for mysql server
    LINK = https://dev.mysql.com/get/mysql-apt-config_0.8.29-1_all.deb
    wget $(LINK)
    # install the mysql server
    FILE_NAME = LINK | cut -d'/' -f5
    sudo dpkg -i $(FILE_NAME)
    sudo apt-get update
    sudo apt-get install mysql-server
    # remove the deb file
    rm $(FILE_NAME)
else
    echo 'mysql is already installed.'
fi

# load environment variables from .env file
source .env

# modify the mysql configuration file
sudo printf "[client]" >> /etc/mysql/my.cnf
sudo printf "user=%s" "$DB_USER" >> /etc/mysql/my.cnf
sudo printf "password=%s" "$DB_PASS" >> /etc/mysql/my.cnf
# create database
mysql -e "CREATE DATABASE IF NOT EXISTS $DB_SDN;"

# crent privileges
mysql -e "CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASS';"
mysql -e "GRANT ALL PRIVILEGES ON $DB_SDN.* TO '$DB_USER'@'localhost' WITH GRANT OPTION;"
mysql -e "FLUSH PRIVILEGES;"

cd backend
# install dependencies
python3 -m pip install -r requirements.txt

cd ..

cd frontend
# install dependencies
npm install
cd ..