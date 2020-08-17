#!/usr/bin/env bash
# This will prepare a web server

# Install nginx
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y

# Create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create fake HTML file
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# ives ownership of /data/ folder to user and group
sudo chown -R ubuntu:ubuntu /data/

# Config NGINX to serve some content
content="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "37i\ $content" /etc/nginx/sites-enabled/default
sudo service nginx reload
sudo service nginx restart
