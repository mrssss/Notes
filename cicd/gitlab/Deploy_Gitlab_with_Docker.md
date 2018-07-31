# 安装Gitlab

1. 创建gitlab工作目录

```bash
mkdir gitlab_volume
```

2. 设置环境变量

```bash
CURRENT_DIR=$(pwd)

# 这条命令只运行一次
# 注意是>>
echo """export GITLAB_CONFIG=$CURRENT_DIR/config
export GITLAB_DATA=$CURRENT_DIR/data
export GITLAB_LOGS=$CURRENT_DIR/logs""" >> ~/.bashrc

source ~/.bashrc
```

3. 运行gitlab-ce容器

```bash
docker run -p 443:443 -p 2222:22 -p 80:80 --name gitlab --volume $GITLAB_CONFIG:/etc/gitlab --volume $GITLAB_LOGS:/var/log/gitlab --volume $GITLAB_DATA:/var/opt/gitlab gitlab/gitlab-ce
```

# 配置Gitlab

> 打开浏览器，输入本机的主机名或IP地址，可以看到gitlab已经启动。

![gitlab启动后界面](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_init_root_passwd.png)

> 这里要求输入的密码是gitlab的管理员账户root的密码。设置密码后，即可登录gitlab账户。

![登录界面](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_login.png)

> 第一次进入界面后可以看到如下界面，我们选择Create a project来创建一个项目

![初次进入gitlab的界面](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_ui.png)

> 创建项目时可以有三种选项：创建空项目，使用模板创建项目，导入项目。我们选择创建空项目。

> 输入项目名，选择项目的可见范围，点击create project按钮就可以创建好我们的第一个gitlab项目了。

![创建项目](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_create_project.png)

> 项目创建好之后，我们会看到下面的界面

![项目界面](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_project_view.png)

> 我们会发现创建出来的项目存在几个问题。

- gitlab提示我们现在没有设置ssh key，所以不能使用ssh的方式pull项目。
- gitlab提供的http下载网址中的主机名称使用的是docker中容器的名称，网络中的主机不能通过该url正常pull项目。

### 设置个人账户的ssh key

1. 检查～/.ssh目录下是否存在id_rsa.pub文件，若存在，该文件的内容就是当前电脑的ssh key，若不存在，则使用以下命令生成ssh key
```bash
ssh-keygen -t rsa -C "your_email@example.com"
```

2. 如图选择账户设置
 
![账户设置](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_personal_setting.png)

3. 将第1步中找到的ssh key复制到文本框中即可，要注意一定要复制  .pub后缀的文件，pub代表的是public，你的公钥，千万别把你的私钥告诉别人。
 
![添加ssh key](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_add_ssh_key.png)


### 配置gitlab主机名

> 为了保证局域网或本地主机能够正确的通过gitlab提供的链接下载项目，我们需要对gitlab进行进一步的配置。

1. 运行该容器的bash

```bash
docker exec -it gitlab /bin/bash
```

2. 打开/etc/gitlab/gitlab.rc文件并将"external_url"变量的值设为你当前的主机名

```python
external_url = "http://qniu-MBP-35D39"
```

> 我们运行该容器的时候已经设置了文件夹的映射，所以在宿主机上对相应的文件进行修改具有同样的效果。

3. 运行gitlab-ctl命令使配置生效

```bash
gitlab-ctl reconfigure
```

4. 回到gitlab网页，我们新建一个项目测试一下，有没有成功修改gitlab的url
 
![修改url](https://raw.githubusercontent.com/mrssss/Notes/master/Resource/cicd/Gitlab/gitlab_external_url_config.png)

> 从图中我们可以看到新建项目的url已经变成了正常的主机名，打开原先创建的项目test会发现项目的url也变成正常的主机名了。说明url已经配置成功了。