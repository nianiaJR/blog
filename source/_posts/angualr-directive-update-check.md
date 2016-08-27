---
title: Angular directive中scope的值更新问题
date: 2016-07-14
categories: Angular
tags: directive-summary
---

### 起因
这是今天在给pipe项目中自己封装的date-picker directive中$scope上的某个Date类型的属性赋值的时候，造成的问题：我在项目中引入了Moment的库，然后我有一个时间控件，而我的directive里面就是存有一这么一个变量：
```
$scope.singleDate = {
	date: {
    	startDate: moment()
    }
}
```
然后在我采用这样的方式更新（例如我有一个向前一天的按钮，那么我的更新方式就如下）：
```
$scope.singleDate.date.startDate.subtract(1, 'days');
```
这个时候问题就来了，按道理一旦我点击一次 向前一天 这个按钮，那么我的date-picker在页面显示的时候会有所更新，可是现在并没有，但是我通过chrome debugger下看见的$scope.singleDate.date.startDate确实是存在改变的。

### 分析
后面经过和前端的同事讨论这个现象，我们发现$scope.singleDate.date.startDate的改变，是存在于这个moment对象实例的原型上的，而非他自己的属性，那么这里也说明Angular的dirty－checking是不针对原型链上的属性值的，想想也是，不然这样的开销未免太大了，会做很多重复工作。

### 解决办法
由于直接使用原moment对象无法使得更新被检测到，所以后面我就每次重新赋一个新的moment对象出来，替换掉原来的，这样更新也就捕捉到了。

### 总结
Angular的dirty-checking是不考虑原型链的，以后在出现类似的情况，均可采用上面的方法，以免出bug。