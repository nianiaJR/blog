---
title: 行为型设计模式 之 观察者模式
date: 2016-12-26
categories: JS设计模式
tags: JavaScript设计模式
---
内容节选自 张容铭 老师的《JavaScript设计模式》
### 观察者模式
又称作 发布－订阅模式 或 消息机制，定义了一种依赖关系，解决了主题对象瑀观察者之间功能的耦合。类似与之前的中介者模式，但观察者模式更强调双向的通信，而中介者模式属于单向的信息通信。

### 代码
```
var Observer = {
	var _messages = {};
	regist: function(type, fn) {
    	if (!_messages[type]) {
        	_messages[type] = [fn];
        } else {
        	_messages[type].push(fn);
        }
    },
    fire: function(type, args) {
    	if(!_messages[type]){
        	return;
        }
        var events = {
        	type: type,
            args: args || {}
        };
        for (var i = 0, len = _messages[type].length; i < len; i++) {
        	_messages[type][i] && _messages[type][i]();
        }
     },
     remove: function(type, fn) {
     	if(_messages[type] instanceof Array) {
        	var i = _messages[type].length - 1;
            for(; i >= 0; i--){
            	_messages[type][i] == fn && _messages[type].splice(i, 1);
            }
        }
     }
};

// 使用
// A
(function() {
	function addMsgItem(e) {
    	var text = e.args.text,
        	ul = $('msg'),
            li = document.createElement('li'),
            span = document.createElement('span');
            li.innerHTML = text;
            span.onclick = function() {
            	ul.removeChild('li');
                Observer.fire('removeCommentMessage', {
                	num: -1
                })
            },
            li.appendChild(span);
            ul.appendChild(li);
    }
    Observer.regist('addCommentMessage', addMsgItem);
})();

// B
(function() {
	function changeMsgNum(e) {
    	var num = e.args.num;
        $('msg_num').innerHTML = parseInt($('msg_num').innerHTML) + num;
    }
    Observer
    	.regist('addCommentMessage', changeMsgNum)
        .regist('removeCommentMessage', changeMsgNum);
})();

// C
(function() {
	$('user_submit').onclick = function() {
    	var text = $('user_input');
        if (text.value === '') {
        	return;
        }
        Observer.fire('addCommentMessage', {
        	text: text.value,
            num: 1
        });
        text.value = '';
    }
})();
```
### 观察者模式 与 中介者模式
从我的理解上，两者在代码形式上是一样的，更多的是行为上的区别，前者是双向的，同一个对象既可以是消息发送者，也可以是消息接收者，后者是单向的，一个发送，一个接收。