---
title: Angular ng-repeat track by的再一次认识
date: 2016-07-12
categories: Angular
tags: directive-summary
tog: true
---

### 起因
这是今天开发遇见的问题，由于我写了一个html片段:

`<div ng-repeat="widget in widgets track by $index"></div>`

后面就出现一个“奇妙的事情”：我的widget是一个个对象，每当我更新对象中的值的时候，按道理，Angular的directive应该是会重新执行一次 `link函数`，可是它却没有，导致不会在我更新了widget内容（实际是创建一个新的widget对象）后，不会再次执行`link函数`，这让我有点纳闷，后面找来前端的同事来帮忙分析一下这个问题，看了一会儿后他让我试着把`track by $index`去掉试一试，一去掉后更新就立即生效了，因为我更新的widget正好，这才让我恍然大悟，原来自己之前一直弄错了track by $index的含义，以前一直以为只要存在数组重复的时候就需要加上这么一句话，然而它有更多的含义。

### 分析
1、首先，Angular的ngRepeat指令，是将枚举的每个片段进行独立render的，例如`ng-repeat="item in items"`，每个item会进行一次render，在我们这里也就是link会执行一次，而后不会再次执行，为了监控变化，Angular会维护一个$hashKey，来映射所对应的item，方便后面的监测变化，而$hashKey是可以自己指定的，比如前面的`track by $index`，以数组的索引来映射item，而在默认不指定的情况下，Angular则会用内部的$id()函数来对item进行一次hash值计算，这里就会限制你在使用默认的track by时，你的枚举对象是不能存在重复的，不然他们的hashKey会冲突。

2、正如我们上面所说，默认情况下每个item只会进行一次render，即使我们后面更改了item的内部属性值，除了一种情况，那就是我们在集合items中，把相应某个位置的item重新new了一个，这里就相当于我们先把这个对应的片段从Dom片段里移除，再加上新的item，而对于新的item，则肯定需要重新render了，所以link函数便会执行。而为什么Angular知道这个是一个移除旧的添加新的item的过程，则是因为之前说的$id()所计算的hashKey的作用。

3、接着，由于之前我仅仅只知道`track by $index`可以用来枚举重复的数组类型，所以自觉地就写上了，而这里就会存在一个问题：一旦你track by index，那么即使你的数据中的某一像item已经是重新new的一个对象了，那么angular也不会重新render，这里可以参考[官方文档](https://docs.angularjs.org/api/ng/directive/ngRepeat)，那这就导致了为啥我已经在对应的位置上new一个widget了，可是它没有angular认为是一个新的需要render的DOM片段, 因为我track by $index。

4、最后，总的来说，`track by $index`是有好处的，因为它避免了不必要的render，而对于有必要的更新，则可以根据别的方式来进行不足，当然，可以使用自己指定的`track by $hashKey`，这样可能会更好，比如如果我的items里面存在重复的项，而我又不想使用`track by $index`,因为他会阻碍我的更新，那么使用自己的$hashKey好处就显现出来了。

### 总结
谨慎的使用track by，根据自己的实现场景来选择对应的$hashKey
