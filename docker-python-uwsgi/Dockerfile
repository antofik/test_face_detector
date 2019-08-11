FROM python:3.6
MAINTAINER antofik                                          
 
ADD supervisor.conf /etc/supervisor/conf.d/app.conf
ADD uwsgi.xml /opt/uwsgi/uwsgi.xml

RUN apt-get update 
RUN apt-get install -y apt-utils build-essential 
RUN apt-get install -y vim
#RUN easy_install pip3
RUN apt-get install -y supervisor --no-install-recommends
RUN pip install uwsgi

ONBUILD ADD . /opt/www/
ONBUILD WORKDIR /opt/www/
#ONBUILD RUN pip install -r requirements.txt
#ONBUILD RUN service supervisor start

CMD ["supervisord", "-n"]

