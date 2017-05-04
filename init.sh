sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello
sudo ln -s /home/box/web/etc/gunicorn_django.py /etc/gunicorn.d/gunicorn_django
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
