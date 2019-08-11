FROM python:3.4
MAINTAINER antofik                                          
 
ADD supervisor.conf /etc/supervisor/conf.d/app.conf
ADD uwsgi.xml /opt/uwsgi/uwsgi.xml
 
RUN apt-get update; apt-get install -y python3.4 python-dev python-setuptools apt-utils build-essential git vim
RUN easy_install pip
RUN apt-get install -y supervisor mysql-client libmysqlclient-dev libpq-dev sqlite3 gcc --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN pip install uwsgi
RUN pip install mysqlclient

ONBUILD ADD . /opt/www/
ONBUILD WORKDIR /opt/www/
ONBUILD RUN pip install -r requirements.txt
#ONBUILD RUN service supervisor start

CMD ["supervisord", "-n"]

