<!-- TOC START min:1 max:5 link:true update:true -->
- [Install and configure](#install-and-configure)
  - [Environment](#environment)
  - [Install](#install)
    - [ubuntu](#ubuntu)
    - [Windows and Mac](#windows-and-mac)
  - [uninstall](#uninstall)

<!-- TOC END -->

---
# Install and configure
---
## Environment

* Linux
* 大硬盘

> Docker是基于Linux内核设计的， 不能直接在Windows和Mac上使用，但Docker的官网上也提供了Mac和Windows版本的Docker，在开源社区中也有一个产品boot2Docker解决了这个问题。

> Docker官方建议在ubuntu系统上运行Docker，因为ubuntu默认支持了AUFS文件系统。

* Linux内核版本最小为3.10

```bash
uname -r
```

---

## Install
### ubuntu
1.使用官网脚本安装

```bash
sudo apt-get update
sudo apt-get install wget

wget -qO- https://get.Docker.com/ | sh
```

2.验证是否安装成功

```bash
sudo docker --version
sudo docker run hello-world
```

3.配置
> Docker Deamon会监听本地的一个socket文件，
> 访问该文件需要root权限，
> 所以执行docker命令都要使用sudo提权。
> 可以通过一下操作来回避掉socket文件没有读写权限的问题。

> 创建Docker组
```bash
groupadd Docker
```
> 将当前用户添加到组中
```bash
usermod -aG Docker $USER
```

### Windows and Mac

> 直接在官网上下载安装包

---

## uninstall

> 卸载安装包和依赖模块

```bash
sudo apt-get autoremove --purge lxc-Docker
```

> 删除配置文件及数据

```bash
rm -rf /var/lib/Docker
```
