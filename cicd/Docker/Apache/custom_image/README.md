# 创建镜像，将html文件复制到容器中，直接运行容器

```bash
docker build -t qniu/webserver:custom .
docker run -d -p 8999:80 --name apache_app qniu/webserver:custom

```