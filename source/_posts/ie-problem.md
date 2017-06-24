---
title: 记一次需求的ie8兼容问题
date: 2017-02-16
categories: Work
tags: ie
---
<img src="http://7xja3v.com1.z0.glb.clouddn.com/feedback.png">
### 前言
这个sprint，松哥临时插了一个用户意见反馈给我做，如上图那样，看起来还挺容易的，所以自己就给估了一天的工时，没曾经想从图片上传，到状态loading以及输入栏的placeholder，处处都有着兼容的问题，晚上都弄挺晚，下面来捋一捋其中出现的一些问题。

### 图片上传
现代的浏览器，要实现ajax上传图片，都是通过XMLHttpRequest2支持的FormData函数对上传图片进行序列号，然后传送到server。而在ie8下，XMLHttpRequest是不支持的，并且也拿不到上传的进度信息，所以加载条也是没法做的。为了上传图片，就需要利用form表单+iframe的形式，利用设置form的target指向一个iframe，然后从iframe里面取回reponseData，目前已有的Web图片上传兼容插件[jQuery Form Plugin](http://malsup.com/jquery/form/):
```
    if (options.iframe !== false && (options.iframe || shouldUseFrame)) {
        // hack to fix Safari hang (thanks to Tim Molendijk for this)
        // see:  http://groups.google.com/group/jquery-dev/browse_thread/thread/36395b7ab510dd5d
        if (options.closeKeepAlive) {
            $.get(options.closeKeepAlive, function() {
                jqxhr = fileUploadIframe(a);
            });
        }
        else {
            jqxhr = fileUploadIframe(a);
        }
    }
    else if ((hasFileInputs || multipart) && fileAPI) {
        jqxhr = fileUploadXhr(a);
    }
    else {
        jqxhr = $.ajax(options);
    }

```
从代码上看，他的兼容处理就是支持FormData的走fileUploadXhr，不支持的就走fileUploadIframe，不过就算利用了iframe来上传图片，如果想要成功得到返回数据的话，对于服务端返回的数据格式也是有要求的，ie8下不能将json直接push到页面，可能会出现下载文件的情况，这里就需要服务端做处理，返回的数据格式应该使用text/html类型，或者直接将数据放到一个textarea标签里面，确保数据正常返回而不触发下载，总之老版本ie下的图片上传需要使用iframe，同时对于上传图片的接口数据返回有要求，需要返回老版本浏览器支持的格式。

### placeholder
ie8下常见的placeholder也是不支持的，模拟的方法也有很多，可以采用在textarea标签背后悬浮一个p标签来做placeholder，这里需要将textarea标签的background稍微做下处理，因为为了不影响正常textarea的focus交互，用z-index把p标签放在textarea后面，又需要显示出p标签，那么就需要将textarea元素标签背景改为透明的，但光是设置`background: none;`或者`background: transparent;`在ie8下会导致z-index失效，使得本来藏在textarea背后的p元素跑出来，影响正常的交互，所以这里还需要使用一张透明的图片来当背景才可以。
```
background: transparent 0 0 repeat scroll url("data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7");

```

### block wrap img
由于inline元素通常是不具有含宽和高意义的，但像图片这种inline元素设置height或者width又有意义，这时候如果一旦外层包了一个block元素，这时候这个block元素的高、宽是不可靠的，不同浏览器可能理解不一样，所以这时候需要规范自己的css书写，确定好高宽，在出现设置子元素定位的时候，因为浏览器对于父级元素的高宽理解不一致，导致内部子元素布局错乱。

### 总结
这次也是由于兼容经验不足，在PM插入需求的时候没有估计好任务量，导致自己弄了半天才发现有的地方是不能满足要求的，这样到回来减少需求代价就大了。而且考虑到兼容ie8的代价，有时候降级处理可能是更好的办法，不能一味的为了满足产品需求，去做一些长期来看很trick，很脏的事，套用松哥的话，该得争取的地方，还是要争取下。毕竟生命是有限的，需求是做不完的。