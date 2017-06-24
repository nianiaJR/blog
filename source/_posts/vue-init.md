---
title: Vue源码初探－vue.js构建、数据绑定、渲染
date: 2017-06-04
categories: Work
tags: vue
toc: true
---

### 前言
零零散散看Vue的源码也有一小段时间了，最初打算采用一个一个文件的硬看，从易到难，不过发现这样看不太科学，对于一些util、config配置文件还好，一旦涉及核心文件，脱离来看，很难看见当前文件在整个项目的联系，越看越懵逼，索性换了一个方式，采用从入口的方式来看，然后以一个简单的例子，比如自己`new Vue({})`来看看具体会发生什么，尝试下来发现好多了。

### 版本V 2.3.3
### vue.js构建过程 － 以dev模式为例
<img src="http://7xja3v.com1.z0.glb.clouddn.com/vue-build.png" width="100%">

### new Vue初始化
初始化的部分几乎均在_init里执行，主要是在实例上添加属性／方法：
1. `initLifeCycle(vm);`初始化$parent、$root、$children、$ref等属性
2. `initEvents(vm);` 初始化event相关属性，如_events
3. `initRender(vm);` 在实例上绑定$createElement方法
4. `callHook(vm, 'beforeCreate');` beforeCreate的hook
5. `initInjections(vm);`
6. `initState(vm);` 进行数据绑定的地方，props、data、computed、watch等
7. `initProvide(vm);`
8. `callHook(vm, 'created');` created的hook
9. `vm.$mount(vm.$options.el);` 开始$mount，将template转化为render，建立watcher部分

### 数据绑定
vue的数据绑定是利用defineProperty来定义getter和setter来实现的，通过值被touch触发getter的过程中，将通过绑在Dep.target上的依赖watcher（computed、render、watch）加入自己的dep数组中，然后一旦相应的值被改变，会触发setter并且通知相应的dep里的watcher进行重新计算。当然针对像数组这样没发定义自己的getter和setter的类型，则是通过封装好的数组方法（slice、push等）来实现的，具体的过程直接看源码会更清晰，这里也就不写了。

### 渲染
前面说到，初始化最后会调用vm.$mount，而这个函数实现最外层部分（以web平台为例），是在==runtime-with-compiler.js==中定义的，该文件部分主要做的事情是将template转化为render函数，而后又继续去调用了原本在==runtime/index.js==中定义的mount方法，具体流程：
1. runtime-with-compiler.js: 调用compileToFunctions将template转化为render函数（最终是一个watcher)，而后继续调用原本在runtime/index已经定义的mount方法。
2. runtime/index: 真正的mount阶段，render会包在一个名叫updateComponent的函数内，最后该函数会`vm._watcher = new Watcher(vm, updateComponent, noop)`建立对应的wacher，然后在render时，因为相关值的touch而被加入对应的watcher，使得一旦值被改变，相应的render也会触发。

### 小结
最简单`new Vue({})`的流程大致是这样了，更详细的部分还需要继续看源码。