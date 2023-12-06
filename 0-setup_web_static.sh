#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

sudo apt update -y
sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo 'IT WORKS!' > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

default_conf="server_name _;"
new_conf="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

sudo sed -i "s|$default_conf|$new_conf|" /etc/nginx/sites-enabled/default
sudo service nginx restart
