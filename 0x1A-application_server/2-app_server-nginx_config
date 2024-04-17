#!/usr/bin/env bash
#configure Nginx to serve your page from the route /airbnb-onepage/

service_config="
[Unit]
Description=unicorn instance to serve web_flask
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/AirBnB_clone_v2/web_flask
Environment='PATH=/usr/bin'
usr/bin/gunicorn --workers 3 --bind unix:web_flask.sock -m 007 wsgi:app
[Install]
WantedBy=multi-user.target
"
sudo touch "/etc/systemd/system/web_flask.service"
chown "$USER":"$USER" "/etc/systemd/system/web_flask.service"
echo "$service_config" > "/etc/systemd/system/web_flask.service"
chown root:root "/etc/systemd/system/web_flask.service"
sudo systemctl start web_flask
sudo systemctl enable web_flask


#proxy request configuration
server_config="
server {
    listen 80;
    server_name web-01.fridausokoya.tech 54.174.181.31 localhost 127.0.0.1;

    location /airbnb-onepage/ {
        include proxy_params;
        proxy_pass http://127.0.0.1:5000;
    }
}"

sudo touch "/etc/nginx/sites-available/web_flask"
chown "$USER":"$USER" "/etc/nginx/sites-available/web_flask"
echo "$server_config" > "/etc/nginx/sites-available/web_flask"
chown root:root "/etc/systemd/system/web_flask.service"
sudo ln -s /etc/nginx/sites-available/web_flask /etc/nginx/sites-enabledsudo systemctl restart nginx
