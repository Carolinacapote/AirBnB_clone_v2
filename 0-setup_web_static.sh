#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
# Create the new folders if they do not exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/
# Create a fake HTML file to test the Nginx configuration
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# Create a symbolic link to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server;/a location /hbtn_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
# Restart nginx
sudo service nginx restart
exit 0
