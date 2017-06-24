---
title: 行为型设计模式 之 中介者模式
date: 2016-12-26
categories: JS设计模式
tags: JavaScript设计模式
---

### 定义 － 中介者模式
通过中介者对象封装一系列对象之间的交互，使对象之间不再相互引用，降低他们之间的耦合。

### 代码
```
// 中介对象
var Mediator = function() {
	// 消息对象
    var _msg = {};
    return {
    	/***
        * 参数 type      消息名称
        * 参数 action    消息回调函数
        ****/
        register: function(type, action) {
        	if (_msg[type]) {
            	_msg[type].push(action);
            } else {
            	_msg[type] = [];
                _msg[type].push(action);
            }
        },
        /***
        * 发布消息
        * 参数 type 消息名称
        ***/
        send: function(type) {
        	if(_msg[type]) {
            	for(var i = 0, len = _msg[type].length; i < len; i++) {
                	_msg[type][i] && _msg[type][i]();
                }
            }
        }
}();

// 单元测试
Mediator.register('demo', function() {
	console.log('first');
});
Mediator.register('demo', function() {
	console.log('second');
});
Mediator.send('demo');
// first
// second
```