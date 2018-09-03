FROM qniu/sshd:debian_jessie

MAINTAINER qniu qniu@splunk.com

ENV DEBIAN_FRONTEND noninteractive

# 安装apache2
RUN apt-get update \
 && apt-get install -y apache2 \
 && apt-get clean \
 && echo "Asia/Shanghai" > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata

ADD run.sh /run.sh
RUN chmod 755 /*.sh

RUN mkdir -p /var/lock/apache2 \
 && mkdir -p /app \
 && rm -rf /var/www/html \
 && ln -s /app /var/www/html

COPY ./publish_html /app

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_SERVERADMIN admin@localhost
ENV APACHE_SERVERNAME localhost
ENV APACHE_SERVERALIAS docker.localhost
ENV APACHE_DOCUMENTROOT /var/www

EXPOSE 80
WORKDIR /app
CMD ["/run.sh"]