#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# Install nginx
apt-get -y update
apt-get -y install nginx
# Create the new folders if they do not exist
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
# Create a fake HTML file to test the Nginx configuration
echo 'Holberton School'> /data/web_static/releases/test/index.html
# Create a symbolic link to the /data/web_static/releases/test/ folder
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i '/listen 80 default_server/a location /hbtn_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
# Restart nginx
service nginx restart
exit 0
