Title: 浏览器缓存问题的了解
Date: 2016-03-13
Category: Work
Tags: 2016

### 前言
上星期整天都在搞关于线上部署新的pipe代码而浏览器缓存导致用户读取页面错误的问题，基于解决问题中查阅的信息，想想在这里做做总结，以方便以后再遇见此类问题的时，可以更加高效。

### Http的缓存机制
http的缓存机制就是为了充分利用第一次从服务器获取的资源，避免重复发送请求来获取相同资源，这样可以降低带宽的使用，由于存在缓存的使用问题，所以就会出现有针对缓存的时效性标记，以下就是几个关于缓存时效性的http字段：
<p style="color:red">关键词：Expires、Cache-Control、 Last-Modified/If-Modified-Since、Etag/If-None-Match</p>

1.<b>Expires:&nbsp;&nbsp;</b> http请求的响应头部字段，例如`Expires: Mon, 14 Mar 2016 03:52:47`，代表资源的失效日期，在这个日期之前，客户端都会认为这个资源的缓存日期是有效的，然而他有一个缺点，因为这里Expires使用的是绝对时间描述，所以当客户端时间与服务端时间不一致时，就会出现问题。因此针对这个问题的补充，Cache-Control字段就出现了。</br>
2.<b>Cache-Control:&nbsp;&nbsp;</b>相对于Expires, Cache-Control字段可以有很多种值。
```
max-age=[秒]：缓存有效期的最长时间，这个参数是基于请求时间的相对时间间隔，所以不存在于服务器时间同步的问题。
no-cache: 这样设置表示每次强制每次请求直接发送給源服务器，而不经过本地缓存版本的校验。
...(Cache-control字段值还有很多，还没用到就不一一列举了)
```
3.<b>Last-Modified/If-Modified-Since:&nbsp;&nbsp;</b>这俩字段是配合Cache-Control来使用的，当资源时效过期时，再次发出请求就会用到它们。
```
Last-Modified：表示响应资源的最后修改时间，通过服务器响应请求时来告诉浏览器对应资源的最后修改时间。
If-Modified-Since：当资源过期时（配合Cache-Control)，通过资源的Last-Modified声明，向服务器发送请求时带上头部字段If-Modified-Since，服务器通过判断最后修改时间是否一致来判断资源是否被改动过，有则响应全部资源、Http 200、并更新Last-Modified; 若没有则响应Http 304(不需要传送实体资源，节省带宽)，让浏览器继续使用所保存的缓存。如果If-Modified-Since时间比服务器时间还晚，会被认为是一个非法请求。
```
<p style="color: red">虽然Last-Modified能解决很多问题，但也是存在缺陷的，因为If-Modified-Since是精确到秒级别的，如果在边界时间内存在文件被修改，浏览器还会错误的继续读取缓存，为了避免这个问题，就又有了Etag/If-None-Match。</p>

4.<b>Etag/If-None-Match:&nbsp;&nbsp;</b>Etag是一个资源特征串，当请求资源时，服务器会在http响应头部加一个Etag字段，代表所请求资源的标记，等着下一次再请求资源时，会在请求的http头部加上If-None-Match字段，传入之前申请到资源的Etag，服务器根据传过来的Etag特征串与现在资源的特征串做对比，如果并为改变则发送304，告诉浏览器资源未更改，继续读缓存；如果不匹配，则发送200以及更新的资源，并传递新的Etag。由于Etag是基于资源内容的特征串，与时间无关，所以可以避免出现Last-modified出现的问题。

5.<b>&nbsp;&nbsp;200(from cache)&nbsp;&nbsp;</b>和<b>&nbsp;&nbsp;304(Not modified)&nbsp;&nbsp;</b>: 这两种状态都是读取缓存，不过前者并未实际向服务器发送了请求，而是根据Expires/Cache-Control来判断的，而后者是通过服务器反馈后再读取的缓存。前者触发可以通过再浏览器地址框键入相同的URL得到，而后者通过刷新URL触发，这是有区别的。

![图解浏览器请求](http://7xja3v.com1.z0.glb.clouddn.com/browser-cache2.png)

### 解决缓存问题
1.<b>`<meta HTTP-EQUIV="Cache-Control" CONTENT="no-cache">`:&nbsp;&nbsp;</b>这段代码的作用是告诉浏览器当前页面不被缓存，每次访问都需要去服务器拉取。不过这段代码据说只有部分浏览器支持，所以他有缺陷。
2.<b>使用query</b>:&nbsp;&nbsp;在获取资源的路径后添加query，例如：`src='pipe.min.js?version=1.1.0`；这样每次上线发布的时候修改query就能保证每次读取的都是新的资源，为了省事避免每次手动修改query字符串，还可以在构建脚本中自动去生成一个随机字符串，使得构建更加自动化。目前我写的项目里采用的就是这样的方式，不过它确实是有缺陷的，具体的可以参考：[基于文件内容的hash版本冗余机制](http://www.infoq.com/cn/articles/front-end-engineering-and-performance-optimization-part1)
3.[基于文件内容的hash版本冗余机制](http://www.infoq.com/cn/articles/front-end-engineering-and-performance-optimization-part1)：由于这个方法我还没实现，也就不多说了。
4.<b>angular-template</b>:&nbsp;&nbsp;虽然采用了第二种方式解决了JS和CSS缓存的问题，不过因为JS和CSS是被我集中打包处理的，所以在用脚本添加query的时候很方便，然而由于在angular的项目里，我会引用很多html的模版文件，它们的索引url分布在各个js文件中，很难用脚本实现自动添加，同时手动添加又不科学。所以此时就想到了是否可以把所有的html都打包到一个文件中，然后索引该文件就好，angular确实有这样的功能，将html片段转为js文件，然后以模块注入的方式，以路径作为字典来索引模版。在Grunt插件中，就有这样的支持：[grunt-html2js](https://github.com/karlgoldstein/grunt-html2js)