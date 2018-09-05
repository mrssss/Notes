<!-- TOC START min:1 max:5 link:true update:true -->
- [Shell](#shell)
  - [UNIX philosophy](#unix-philosophy)
  - [UNIX best practice](#unix-best-practice)
  - [Shell Script](#shell-script)
    - [Advantage](#advantage)
    - [Simple sample](#simple-sample)
    - [Syntax](#syntax)

<!-- TOC END -->

---
# Shell
---
## UNIX philosophy

* 将中型到大型的问题拆成较小的部分。
* 使用工具箱中现成的工具解决问题。
* 针对要解决的问题选择专业的软件工具。

**学习Shell的基本语法和学习UNIX中的核心工具箱用法同等重要**

* shell是粘合剂，整体的功能比各部分加起来的总和还强大

## UNIX best practice

* 一次做好一件事
* 处理文本行， 不要处理二进制数据
* 使用正则表达式
* 默认使用标准输入/输出
* 避免喋喋不休
* 输出格式必须与可接受的输入格式一致
* 让工具去做困难的部分
* 构建特定工具前， 先想想

## Shell Script

> Shell脚本最常用于系统管理工作，或者是用于结合现有的程序以完成小型的，特定的工作。

### Advantage

* 简单性
* 可移植性
* 开发容易

### Simple sample

```bash
$ cat > nusers
who | wc -l
Ctrl-D
$ chmod +x nusers
$ ./nusers
```

### Syntax
* [Shell脚本语法](./shell.md)
