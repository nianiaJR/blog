---
title: 行为型设计模式 之 模板方法模式
date: 2016-12-16
categories: JS设计模式
tags: JavaScript设计模式
---

来自张容铭老师的《JavaScript设计模式》
### 定义 - 模板方法模式
父类中定义最初始的骨架，而将一些实现步骤推迟到子类中，使得子类可以不改变父类的算法结构的同时可重新定义算法中某些实现步骤。

### 代码
```
<!DOCTYPE html>
<head>
    <script>
        // 模板类 基础提示框渲染
        function Alert (config) {
            if (!config) return;
            // 设置内容
            this.content = config.content;
            // 创建提示框面板
            this.panel = document.createElement('div');
            // 创建提示内容组件
            this.contentNode = document.createElement('p');
            // 创建确定按钮组件
            this.confirmBtn = document.createElement('button');
            // 创建关闭按钮组件
            this.closeBtn = document.createElement('b');
            // 为提示面板添加类
            this.panel.className = 'alert';
            // 为关闭按钮添加类
            this.closeBtn.className = 'a-close';
            // 为确定按钮添加类
            this.confirmBtn.className = 'a-confirm';
            // 为确定按钮添加内容
            this.confirmBtn.innerHTML = config.confirm || '确认';
            // 为提示内容添加文本
            this.contentNode.innerHTML = this.content;
            // 点击确定按钮执行方法 如果config中有success方法则为success方法，否则为空函数
            this.success = config.success || function () {};
            // 点击关闭按钮执行方法
            this.fail = config.fail || function () {};
        }

        Alert.prototype = {
            init: function () {
                this.panel.appendChild(this.closeBtn);
                this.panel.appendChild(this.contentNode);
                this.panel.appendChild(this.confirmBtn);

                document.body.appendChild(this.panel);

                this.bindEvent();

                this.show();

                return this;
            },
            bindEvent: function () {
                var that = this;
                this.closeBtn.onclick = function () {
                    that.fail();
                    that.hide();
                }

                this.confirmBtn.onclick = function () {
                    that.success();
                    that.hide();
                }
            },
            hide: function () {
                this.panel.style.display = 'none';
            },
            show: function () {
                this.panel.style.display = 'show';
            }
        }

        // 根据模板，创建衍生类
        function RightAlert (config) {
            Alert.call(this, config);
            this.confirmBtn.className = this.confirmBtn.className + ' right';
        }
        RightAlert.prototype = new Alert();

        function TitleAlert (config) {
            Alert.call(this, config);
            this.title = config.title;
            this.titleNode = document.createElement('h3');
            this.titleNode.innerHTML = this.title;
        }
        // 继承基本提示框方法
        TitleAlert.prototype = new Alert();
        TitleAlert.prototype.init = function () {
            this.panel.insertBefore(this.titleNode, this.panel.firstChild);
            Alert.prototype.init.call(this);

            return this;
        }

        // 继承类继续作为模板类使用
        function CancleAlert(config) {
            TitleAlert.call(this, config);
            this.cancel = config.cancel;
            this.cancelBtn = document.createElement('button');
            this.cancelBtn.className  = 'cancel';
            this.cancelBtn.innerHTML = this.cancel || '取消';
        }
        CancleAlert.prototype = new Alert();
        CancleAlert.prototype.init = function () {
            TitleAlert.prototype.init.call(this);
            this.panel.appendChild(this.cancelBtn);

            return this;
        }
        CancleAlert.prototype.bindEvent = function () {
            var that = this;
            TitleAlert.prototype.bindEvent.call(this);
            this.cancelBtn.onclick = function () {
                that.fail();
                that.hide();
            }
        }
        setTimeout(function () {
         document.body.appendChild(
                (new Alert({
                    title: '提示标题',
                    content: '提示内容',
                    success: function() {
                        console.log('ok');
                    },
                    fail: function() {
                        console.log('cancel');
                    }
                })).init().panel)

         document.body.appendChild(
                (new CancleAlert({
                    title: '提示标题',
                    content: '提示内容',
                    success: function() {
                        console.log('ok');
                    },
                    fail: function() {
                        console.log('cancel');
                    }
                })).init().panel)
        }, 100);
    </script>
</head>
<body>
</body>

```