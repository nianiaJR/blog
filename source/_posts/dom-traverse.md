---
title: DOM遍历－NodeIterator与TreeWalker的使用
date: 2015-8-24
categories: JavaScript
tags: DOM遍历
---

### 前言
最近高级教程关于DOM的章节，读到了关于DOM遍历DOM2级遍历的讲解，觉得很有用，拿来小结一下，总的来说就是NodeIterator和TreeWalker两个遍历DOM类型的使用，这是在DOM2级新增的类型。

### 浏览器的支持
使用之前最好先检测一下各个浏览器的支持情况，对于老版本浏览器，可以参照书中的详细描述，不过IE并不支持DOM遍历。在一般的浏览器中，可以用如下代码进行简单的检测，支持情况：
```
var supportsTraversals = document.implementation.hasFeature("Traveral", "2.0");
var supportsNodeIterator = (typeof document.createNodeIterator == "function");
var supportsTreeWalker = (typeof document.createTreeWalker == "function");
```

### NodeIterator
```
// 使用document.createNodeIterator(root, whatToShow, filter, entityReferenceExpansion)来创建NodeIterator的实例
// root: 想要作为搜索起点的树中的节点
// whatToShow: 表示要访问哪些节点的数字代码，在NodeFilter里面有配置好的变量可用（例如NodeFilter.SHOW_ELEMENT)
// filter: 一个NodeFilter对象，活着一个表示应该接受还是拒绝某种特定节点的函数
// entityReferenceExpansion: 布尔值，表示是否要扩展实体引用，这个参数在HTML页面中没有用，因为其中的实体引用不能扩展

// 例子：
HTML 片段：
<div id="test">
	<p>test</p>
    <ul>
    	<li>test1</li>
        <li>test2</li>
    </ul>
</div>

javascript:
var div = $('#test');
var iterator = document.createNodeIterator(div, NodeFilter.SHOW_ELEMENT, null, false); //只遍历元素节点
var node = iterator.nextNode(); // NodeIterator对象有两个方法一个是nextNode, 一个是previousNode， 不言而喻
while(node !== null) {
	alert(node.tagName);
    node.nextNode();

}

```

###TreeWalker
一个更高级的NodeIterator, 除了nextNode()和previousNode()在内的功能外，还提供不同方向遍历DOM结构的方法：
```
parentNode():        // 遍历到当前节点的父亲节点；
firsrtChild();       // 遍历到当前节点的第一个子节点；
lastChild():         // 遍历到当前节点的最后一个子节点；
nextSibling():       // 遍历到当前节点的下一个同辈节点；
previouseSibling():  //遍历到当前节点的上一个同辈节点；
```

创建TreeWalker对象使用document.createTreeWalker()方法， 这个方法接受四个参数，与NodeIterator相同。
除了能做到和NodeIterator上述代码一样的事情外，TreeWalker还能做一些更加巧妙的事情：

```
HTML片段:
<div id="test">
	<p>test</p>
    <ul>
    	<li>test1</li>
        <li>test2</li>
    </ul>
</div>


javascript:
var div = $('#test');
var walker = document.createTreeWalker(div, NodeFilter.SHOW_ELEMENT, null, false);

walker.firstChild(); // 转到<p>
walker.nextSibling(); // 转到<ul>

var node = walker.firstChild(); // 转到第一个<li>
while (node !== null) {
	alert(node.tagName);
    node = walker.nextSibling();
}

var filter = function(node) {
	return node.tagName.toLowerCase() == 'li' ?
    	NodeFilter.FILTER_ACCEPT ：
        NodeFilter.FILTER_REJECT;
};

PS: 注意如果在调用createTreeWalker函数时，有添加非空的filter参数，在定义其函数时，注意NodeFilter.FILTER_REJECT的使用：它会跳过相应节点及该节点的整个子树，注意和NodeFilter.FILTER_SKIP区别开来。如果将上面这个filter加入到刚才的createTreeWalker函数调用里面，意味着遍历会跳过整个div，所以遍历就终止了。

```

