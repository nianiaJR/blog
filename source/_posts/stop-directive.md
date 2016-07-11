---
title: angular:一个用于阻止事件冒泡的directive
date: 2015-8-11
categories: Angular 
tags: directive-summary
---

### 起因
在做数据筛选框的时候，在点击一个输入框聚焦时，需要在输入框下显示出一个下拉提示，一旦在非输入框的部位点击后，该下拉框需要消失，于是我在最外层绑定了一个click事件，用于触发让下拉框消失。但这会导致原本点击聚焦内部输入框时显示的下拉框会因为事件冒泡到外部收起来，形成一个“正”、”负“抵消的态势。因此就会需要针对输入框那部分的区域，阻止事件冒泡。
![http://7xja3v.com1.z0.glb.clouddn.com/stopevent1.png](http://7xja3v.com1.z0.glb.clouddn.com/stopevent1.png)
![http://7xja3v.com1.z0.glb.clouddn.com/stopevent2.png](http://7xja3v.com1.z0.glb.clouddn.com/stopevent2.png)

### 制作一个用于阻止事件冒泡的directive
```
JS:
.directive('stopEvent', function () {
    return {
        restrict: 'A',
        link: function (scope, element, attr) {
            if(attr && attr.stopEvent)
                element.bind(attr.stopEvent, function (e) {
                    e.stopPropagation();
                });
        }
    };
 });
HTML:
<a ng-click='expression' stop-event='click'>
```
