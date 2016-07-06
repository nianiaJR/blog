Title: 围住浮动元素的三种方法
Date: 2015-7-25
Category: CSS
Tags: 2015, summary
Slug: surround-floating-element

### 前言
从《css设计指南》中读到的有借鉴意义的清除浮动元素的三种方法,要想更具体可以看原书，大量css实例应用。

### 1.为父元素添加overflow:hidden
```
// 这里是overflow:hidden另一隐蔽作用，可以迫使父元素包含其浮动的子元素。
HTML:
<section>
	<img src="">
    <p>xxx</p>
</section>
<footer>xxx</footer>

CSS:
img { float: left; }
section { overflow: hidden; }
```
### 2.同时浮动父元素
```
// 浮动父元素后，不管其子元素是否浮动，它都会紧紧包围子元素，因此需要用
// width: 100%让section与浏览器同宽
HTML:
<section>
    <img src="">
    <p>xxx</p>
</section>
<footer>xxx</footer>

CSS:
img { float: left; }
section {
	float: left;
    width: 100%;
}
```
### 3.添加非浮动的清除元素
```
HTML:
// 给父元素的最后添加一个非浮动的子元素，然后清除
<section>
	<img src="">
    <p>xxx</p>
    <div class="clear_me"></div>
</section>
<footer>xxx</footer>

CSS:
img { float: left; }
.clear_me {
	clear: left;
}
```
### 4.一种更为巧妙的清除浮动元素的写法
```
HTML:
<section class="clearfix">
	<img src="">
    <p>xxx</p>
</section>
<footer>xxx<footer>

CSS:
img { float: left; }
.clearfix:after {
	content:".";
	display: block;
    height: 0;
    visibility: hidden;
    clear: both;
}
```

