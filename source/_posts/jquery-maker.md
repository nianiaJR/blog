---
title: 一段模拟jQuery获取DOM元素的代码
date: 2017-01-04
categories: JS设计模式
tags: JavaScript设计模式
---

### 模拟jQuery获取元素
就我们的观察，$('#id')访问获取的元素，返回的往往是一个包含dom元素的数组，并且绑定有很多的方法，下面我们就通过原生的js来实现这么一个事情。

### 一个小例子
下面是模仿一段jQuery的代码
```
<!DOCTYPE HTML>
<html>
    <head></head>
    <body>
        <p id="demo">1</p>
        <p id="test">2</p>
    </body>
    <script>
         var jQuery = function (selector) {
            return new jQuery.fn.init(selector); // 使用new是为了保证每次访问都是独立的一个对象，而不会相互干扰
         }
         jQuery.fn = jQuery.prototype = {
             constructor: jQuery,
             init: function (selector) {
                this[0] = document.getElementById(selector); // 通过this[0]来存获取的对象，这样既能返回访问的对象，又可以return this形成链式调用
                this.length = 1; // 数组的特征
                return this;
             },
            length: 2, // 一个数组所应该拥有的特征方法及属性
            push: [].push,
            sort: [].sort,
            splice: [].splice,
            size: function() {
                return this.length;
            }
         };
        jQuery.fn.init.prototype = jQuery.fn; //为了保证new完以后，对象还拥有原有的方法
        console.log(jQuery('demo'));
    </script>
</html>

```