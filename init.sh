sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

gunicorn -c /home/box/web/etc/gunicorn_ask.conf ask.wsgi:application &
