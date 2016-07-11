---
title: npm－我碰到的那些坑
date: 2015-7-7
categories: Tool
tags: npm-summary
---

### 前言
坑不想踩两遍，难搜的东西也不想重复搜，总之就是为了提升工作效率，如果有错误，非常感谢能指出来，错误不重犯就是拯救绳命啊。

### 总结
**1.`npm install`**
*如果在一个目录下启了这个命令，不要中途终止掉，一旦终止掉最好就把该目录下：rm -rf node_modules 文件整个清空重下，否则再次npm install是不会覆盖下载到一半的文件并且不全的，如果你在启动服务的时候发现曝出有关于node_modules里面缺少什么package的时候，可以联想一下是否是这个地方出现了问题。*
P.S: Angular官方的教程里耶多次警告过类似的问题，不过是关于bower的，也需要注意一下:
![npm install重复启动问题](http://7xja3v.com1.z0.glb.clouddn.com/npm1.png)
[链接在这里](https://docs.angularjs.org/tutorial/step_11)

**2.`npm config set registry https://registry.npm.taobao.org`**
*由于国内特殊的网络原因，npm的默认源是：http://www.npmjs.org/ ，包的下载速度慢得跟狗屎了，这个时候可以换一下源，国内有好多源，据说更新速度不差基本不会影响什么，上面就是一个。
P.S: `$vim ~/.npmrc`在这里面也可以修改地址。*

**3.`npm config get registry`**
*可以查看源地址*
