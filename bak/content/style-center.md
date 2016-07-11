Title: css元素居中小结
Date: 2015-08-30
Category: CSS
Tags: 2015, summary
Slug: css-style-center

### 前言
昨天面试被问到了，由于平常都是边实验边写，没怎么总结，所以面试被问到的时候答得很差劲，现在来做一下总结，下次再问到就不会那么无厘头了，糟糕的感觉不想来第二遍。

ps: 大部分按着这篇博文的作者思路实现了一遍, 做了一些修改：[http://www.hacke2.cn/div-center/](http://www.hacke2.cn/div-center/)

### 水平居中
场景一：行内元素嵌套在一个div中时，需要居中行内元素。
使用：`text-align: center;`

```
css:
.center {
	text-align: center;
}
html:
<div class=".center" style="border: 1px solid;">
    <a style="background-color: #A7E4A7;">这是要居中的块</a>
	<a style="background-color: #B6C1B6;">这是另一个要居中的块</a>
</div>
```

<div class=".center" style="border: 1px solid; text-align: center;"><a style="background-color: #A7E4A7;">这是要居中的块</a> <a style="background-color: #B6C1B6;">是另一个要居中的块</a>
</div>

场景二：对于inline-block元素居中。
使用：`text-align: center;`
<div class="center" style="
    margin: 0 auto;
    text-align: center; border: 1px solid
"> <p style="display: inline-block; background-color: #A7E4A7; margin: auto;">inline-block1</p> <p style="display: inline-block; background-color: #9FA517; margin: auto;">inline-block2</p> <p style="display: inline-block; background-color: #B6C1B6; margin: auto;">inline-block3</p>
</div>

场景三：对于定宽元素的居中
使用: `margin: 0 auto;` 或则不刻意的话`margin: auto;`也是可以的。
```
css:
.center {
	margin: 0 auto;
}
html:
<div class="center" style="background-color: #A7E4A7; width: 80px; margin: auto;">
	<p>我要居中</p>
</div>
```
<div class="center" style="background-color: #A7E4A7; width: 80px; margin: auto;"><p>我要居中</p></div>

场景四：包在弹性盒子内的元素居中
使用：`display: flex; justify-content: center;`
```
css: {
	.center {
    	display: flex;
        justify-content: center;
    }
}

html:
<div class="center">
  <p>flex1</p>
  <p>flex2</p>
  <p>flex3</p>
</div>
```
<div class="center" style="display: flex; justify-content: center;"><p style="background-color: #A7E4A7">flex1</p>&nbsp;<p style="background-color: #9FA517">flex2</p>&nbsp;<p style="background-color: #B6C1B6">flex3</p>
</div>

### 垂直居中
场景一：单一行内元素的居中，让line-height与height值设置一致
使用：`inline-height`
```
css: {
	.center {
   		inline-height: 50px;
    }
}
html:
<div style="height: 50px; border: 1px solid black;">
	<span class="center">垂直居中</span>
</div>
```
<div style="border: 1px solid black;"><span style="line-height: 50px; height: 50px;">垂直居中</span></div>

场景二：多行行内元素垂直居中
使用：`display: table-cell; vertical-align: middle;`
```
css:
.center {
	width: 200px;
    height: 50px;
    display: table-cell;
    vertical-align: middle;
}
<div style="border: 1px solid red;" class="center">
	<a>xxx</a><a>xxx</a><a>xxxxxxx</a><a>xxx</a><a>xxx</a><a>xxx</a><a>xxx</a><a>xxx</a><a>xxx</a>
</div>
```
<div style="width: 200px; height: 50px; border: 1px solid red; display: table-cell; vertical-align: middle;"><a>xxx</a><a>xxx</a><a>xxxxxxx</a><a>xxx</a><a>xxx</a><a>xxx</a><a>xxx</a><a>xxx</a><a>xxx</a></div>

场景三：已知高度的块级元素居中
使用： `margin-top: -height/2;`
```
css: {
	position: absolute;
	height: 20px;
    top: 50%;
	margin-top: -10px;
}
html:
<div style="height: 50px; border: 1px solid; position: relative;">
	<div style="height: 20px; background: #A7E4A7;" class="center">已经知道高度的快级元素</div>
</div>
```
<div style="height: 50px; border: 1px solid; position: relative;">
	<div style="height: 20px; background: #A7E4A7; position: absolute; top: 50%; margin-top: -10px;">已经知道高度的快级元素</div>
</div>

场景四：未知高度的块级元素居中
使用：`transform: translateY(-50%);`
```
css: 
.center{
	position: absolute;
    top: 50%;
	-webkit-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    transform: translateY(-50%);
}

<div style="height: 50px; border: 1px solid; position: relative;">
	<div style="width: 200px; background: #B6C1B6;" class="center">未知高度块元素</div>
</div>
```
<div style="height: 50px; border: 1px solid; position: relative;">
	<div style="width: 200px; background: #B6C1B6; position: absolute; top: 50%; -webkit-transform: translateY(-50%);  -moz-transform: translateY(-50%) transform: translateY(-50%)">未知高度块元素</div>
</div>

### 水平垂直居中
场景一：已知高度的元素
使用：将元素绝对定位，然后`top: 50%; left: 50%; margin-top: -height/2; margin-left: -width/2;`
<div style="height: 50px; border: 1px solid black; position: relative"><div style="height: 20px; width: 200px; position: absolute; top: 50%; left: 50%; border: 1px solid red; margin-top: -10px; margin-left: -100px">已知高度宽度块元素</div>
</div>

场景二：被包含在flex盒中，已知高度，宽度的元素
使用： `display: flex; justify-content: center; align-items: center;`
```
css:
.center {
	display: flex;
    justify-content: center;
    align-items: center;
}

html: 
<div style="height: 50px; border: 1px solid black;" class="center">
	<div style="border: 1px solid red; width: 200px; height: 20px;">
    	flex包含的元素
    </div>
</div>
```
<div style="height: 50px; border: 1px solid black; display: flex; justify-content: center; align-items: center;"><div style="border: 1px solid red; width: 200px; height: 20px;">flex包含的元素</div>
</div>

场景三：未知高度，宽度的元素
使用： 绝对定位＋translate
```
css:
.center {
	position: absolute;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    -moz-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
}
html:
<div style="position: relative; height: 50px; border: 1px solid black">
	<div style="border: 1px solid red;" class="center">
    	高,宽未知的元素
    </div>
</div>
```
<div style="position: relative; height: 50px; border: 1px solid black"><div style="border: 1px solid red; position: absolute; top: 50%; left: 50%; -webkit-transform: translate(-50%, -50%); -moz-transform: translate(-50%; -50%); transform: translate(-50%; -50%);">高,宽未知的元素</div>
</div>

### 总结
总的来说，不论水平居中还是垂直居中，通用来看，都分为 尺寸已知 和 尺寸未知 两种情况，在知道尺寸的情况下都可以通过绝对定位先位于垂直或者水平的中心`top: 50%;` or `left: 50%;`；然后通过为`margin-top: -height/2` 或者 `margin-left: -width/2;` 来平衡元素本身所占用的区域面积，以此来达到平衡。在尺寸未知的情况下，依旧遵循这样的思路，不过这里需要借助`transform：translateX(-50%)` or `transform: translateY(-50%)`来实现和已知尺寸的margin操作，不过这里需要注意浏览器的支持情况。
同时在已知尺寸时，还可以通过设置父级元素的样式布局来影响子元素的布局，比如`text-align：center`对于内部行类元素的居中影响。或者像是`display: table-cell; vertical-align: middle;`这样利用改变元素性质来拥有某些居中属性，达到居中效果。又或者如设置父元素`display: flex;`， 成为一个弹性盒，再通过`justify-content: center;`水平居中控制，`align-items: center;`垂直居中控制，以此来实现居中。
剩下的就是一些零散的居中技巧了，比如对有尺寸的元素`margin: auto;`到达居中目的，或者对单行内元素，设置`line-height`的值与父亲元素高度相同，可以达到垂直居中效果。

以上便是这次居中的总结，希望再接再厉。
