# Ansible

## What is Ansible

> Ansible是一个IT自动化的工具，可以将运维的流程写在playbook中，然后通过ssh连接远程的计算机自动执行相应的操作。

* Save time and be more productive
* Eliminate repetitive tasks
* Fewer mistakes & errors
* Improve collaboration and job satisfaction

> Ansible默认使用本地的OpenSSH进行远程通信，并默认假定你使用SSH Key进行远程连接。

## Installation

```python
pip install ansible
```

## Configure

> Ansible的配置文件名为ansible.cfg。该文件用于定义各种通用的变量。

* ansible.cfg查找顺序

1. ANSIBLE_CONFIG环境变量所指定的文件
2. ./ansible.cfg
3. ~/.ansible.cfg
4. /etc/ansible/ansible.cfg

### [配置文件模板](./ansible.cfg

## Playbooks

> Playbooks是Ansible的配置，部署，编排语言。它描述了我们希望目标主机执行的动作序列。可以看作一种实施方案。

* [Playbooks 的最佳实践](https://github.com/ansible/ansible-examples)

> Playbooks的格式是YAML。

> playbook由一个或多个“plays”组成。它的内容是一个以“play”为元素的列表。
