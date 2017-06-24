---
title: 行为型设计模式 之 命令模式
date: 2016-12-22
categories: JS设计模式
tags: JavaScript设计模式
---
来自张铭容老师的《JavaScript设计模式》
### 定义 - 命令模式
通过输入符合规定的参数，然后产出对应的需求，将请求与实现解耦，并封装成独立的对象。常常用在HTML组件生成阶段。

### 代码 - 一段视图创建的过程
```
var viewCommand = (fucntion() {
	var tpl = {
    	product: [
        	'<div>',
            	'<img src="{#src#}"/>',
                '<p>{#test#}</p>',
            '</div>'
        ].join('')，
        title: [
        	'<div class="title">',
            	'<div class="main">',
                	'<h2>{#title#}</h2>',
                    '<p>{#tips#}</p>',
                '</div>',
            '</div>'
        ].join('')
    },
    // 格式化字符串缓存字符串
    html = '';
   	function formateString(str, obj) {
    	return str.replace(/\{#(\w+)#\}/g, function(match, key) {
        	return obj[key];
        })
    }
    var Action = {
    	create: function(data, view) {
        	if (data.length) {
            	for (var i = 0, len = data.length; i < len; i++) {
                	html += formateString(tpl[view], data[i]);
                }
            } else {
            	html + = formateString(tpl[view], data);
            }
        },
        display: function (container, data, view) {
        	// 如果传入数据
            if (data) {
            	this.create(data, view);
            }
            // 展示模块
            document.getElementById(container).innerHTML = html;
            html = '';
        }
    };
	
    // 命令接口
    return function excute(msg) {
    	msg.param = Object.prototype.toString.call(msg.param) === "[Object Array]" ? msg.param : [msg.param];
        Action[msg.command].apply(Action, msg.param);
    }
})();

// 实际应用
// 产品数据
var productData = [
	{
    	src: 'command/02.jpg',
        text: '绽放的桃花'
    },
    {
    	src: 'command/03.jpg',
        text: '阳光下的温馨’，
    }
]，
titleData = {
	title: '夏日里的一片温馨'，
    text： '暖暖的温泉带给人们家的感受。'
}；
viewCommand({
	command: 'create',
    param: ['title', titleData, 'title']
});
viewCommand({
	command: 'create',
    param: [{
    	src: 'command/01.jpg',
        text: '迎着朝阳的野菊花'
    }, 'product']
});
viewCommand({
	command: 'display',
    param: ['product', productData, 'product']
});
```