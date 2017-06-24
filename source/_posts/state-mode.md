---
title: 行为型设计模式 之 策略模式
date: 2016-12-21
categories: JS设计模式
tags: JavaScript设计模式
---

来自张容铭老师的《JavaScript设计模式》
### 定义 - 策略模式
算法簇，将定义的一组算法封装起来，算法间相互独立，提供一个接口，通过传入不同的策略请求，输出对应的策略算法，还可以提供可以动态添加算法的接口，使得策略模式更加灵活。

### 代码
```
// 一组简单的表单验证算法簇
var InputStrategy = function () {
	var strategy = {
        notNull: function (value) {
            return /./.test(value) ? '' : '请输入内容';
        }，
        number: function (value) {
            return /^[0-9]+(\.[0-9]+)?$/.test(value) ? '' : '请输入数字';
        },
        phone: function (value) {
            return /^\d{3}\-\d{8}$|^\d{4}-\d{4}\-\d{7}$/.test(value) ? '' : '请输入正确的电话号码格式，如：010-12345678 或 0418-1234567’；
        }
    },

    return {
    	check: function (type, value) {
        	value = value.replace(/^\s+|\s+/g, '');
            // 利用字典索引的形式，输出对应算法模块
            return strategy[type] ? strategy[type](value);
        }，
        // 提供增加算法模块的接口
        addStrategy: fcuntion(type, fn) {
        	strategy[type] = fn;
        }
    }
}
```