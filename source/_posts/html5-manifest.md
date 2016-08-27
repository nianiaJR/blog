---
title: HTML5之manifest的应用
date: 2016-07-19
categories: HTML5
tags: manifest
---

### 前言
在pipe的日常开发中，总会遇见这么一个问题：有时候已经更新了代码，可在浏览器端看到的页面还是老的代码，这有时候会让人比较尴尬，尤其是后端同学刚开始写前端的时候，明明自己代码没有错，出现这么一个怪异的现象，总是让别人怀疑人生...对于浏览器缓存，虽然在线上部署的时候我已经采用了加版本号的办法，让 js 和 css在每次上线部署的时候都不会读取缓存，至于html也采用了特殊的办法来转化成js文件的方式杜绝了缓存的读取。然后在dev模式下，由于是我一个人开发，我选择了得过且过...每次强制刷新浏览器就好，现在人多了,看来是得换个法子了。然后我就想到了manifest，因为看见隔壁张导他们都是这么用的，所以就跟着效仿。

### 200 (from cache) 与 304 Not Modified
在说manifest特性前，这里先说一说这两个状态码的区别，前者200（from cache)说明响应是来自缓存的，并且没有访问服务器，一般本地能确认资源是新鲜的话，直接读取缓存能极大的缩短资源请求速度。而后者304 Not Modified也是读取缓存，不过浏览器事先与服务器进行了确认，认定资源是新鲜的。两者的主要区别在这里。他们之间机制，之前也有写过[浏览器缓存](http://www.liangjiarui.com/2016/03/13/browser-cache/)

### manifest
这是HTML5引入的应用程序缓存，用来控制浏览器的缓存，嗯？咱这里是需要干掉缓存。manifest一般是这么使用的：
```
<!DOCTYPE HTML>
<html manifest="app.appcache">
...
</html>
```
<p style="color: red;">需要注意的是，浏览器会缓存带有manifest属性的文件</p>
![manifest缓存from cache](http://7xja3v.com1.z0.glb.clouddn.com/cache.png)

<p style="color: green">如图来看，我在落地页加上了这个属性，那么浏览器就会首次加载完以后，后续的访问就直接从cache里面取了，而不再与服务器打交道，所以这里就需要注意，每次上线重新部署服务器时，如果落地页有修改，需要手动更新manifest文件，不然落地页依然会读取cache缓存。一旦更新了manifest文件，浏览器在读取缓存的时候，会先向服务器确认自己的manifest文件是最新的，不然需要全部更新manifest的缓存内容。</p>

### app.appcache文件：
```
CACHE MANIFEST
CACHE:
# 这里定义要缓存的文件，一个文件名一行
NETWORK：
# 这里定义绕过缓存需要直接从服务器取的
FALLBACK:
# a.url b.url  这里指当a.url不可用的时候，则使用b.url的方案
```

### 然而
manifest虽然是HTML5的特性，然而在了解问题的过程中，我发现它好像已经被标准废弃了。。。虽然有浏览器还在支持：
![](http://7xja3v.com1.z0.glb.clouddn.com/manifest-deprecated.png)
[具体的可以看MDN，这是一个悲伤的故事](https://developer.mozilla.org/en-US/docs/Web/HTML/Using_the_application_cache)
