# 不创建镜像，通过挂载静态页面到容器中运行Apache container

```bash
cd publish_html
docker run -d -p 8999:80 --name apache_app -v "$PWD": /usr/local/apache2/htdocs/ httpd:2.4
```

# 创建镜像，将html文件复制到容器中，直接运行容器

```bash
docker build -t qniu/webserver:httpd .
docker run -d -p 8999:80 --name apache_app qniu/webserver:httpd
```