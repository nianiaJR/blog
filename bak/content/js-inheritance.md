Title: 继承的模式
Date: 2015-8-13
Category: JavaScript
Tags: 2015, summary
Slug: js-inheritance

### 前言
虽然说javascript是原型继承的，但不同的写法，所代表的意思会有着很大差别，以下是常见的继承代码表现形式。

### 伪类
之所以称作伪类是因为它在模仿类继承语言，先去写一个构造函数，然后通过new关键字来生成一个实例对象，在这里个人认为new是伪类继承模式最具代表性的因素。
```
// 先创建一个父“类”
var Parent = function (name){
	this.name = name;
};
// 在原型上创建一个方法
Parent.prototype.getName = function(){
	return this.name;
};
// 构造另一个伪类来继承父“类”
var Child = function (name){
	this.name = name;
};
// 继承
Child.prototype = new Parent();
// 创建实例对象
var child = new Child("test");
// 继承了父类的方法
child.getName();// "test"
```
以上便是使用伪类来继承的方法，正如《javascript语言精粹》上说的那样，它有点奇怪，因为原型继承的思想本是对象继承对象，但这里却在中间夹杂着一个构造函数，通过构造函数来产生新的对象。而且它很容易出错，一旦在构造的过程中少了new，那么直接函数调用，这样函数里的this就会指代为全局变量，造成变量污染而不易被发现，例如`(Parent(name){this.name=name;})(); //直接函数调用，this会被指代为全局的，就造成了污染`

另外，这里还存在着隐私的保护问题，因为所有的变量都是可以从外部被访问的，很容易出问题。

### 简单的原型继承
简单的说就是去掉构造函数的模式，不再使用`new`来创建一个对象，而是采用对象字面量或者`Object.create()`来创建对象，至少避免了`new`可能遗忘而导致的环境污染问题。
```
// 通过对象字面量来创建一个父亲对象
var parent = {
	name: 'test',
    getName: function (){
    	return this.name;
    }
};

// 通过parent对象来构建儿子对象，儿子会继承他的属性及方法
var child = Object.create(parent);
child.name = 'test2'; //可以重写父对象属性
child.getName(); // test2
```
相比于之前伪类的继承方法，这样的代码表达更能体现原型继承的思想：一个新的对象可以继承一个已存在的对象，是对象与对象之间的关系，没有类，也不存在构造函数。

但同样，上面依旧存在着隐私保护的问题，我们接着往下面看，通过如何通过函数构造模块来保护私有变量。

### 函数化
对闭包的理解，内部函数可以引用外部函数的值，可以起到外部函数变量的生命延长以及隐藏不被外部获取的效果，这里正是利用了这一点。通过将设定为私有的那些变量，放在外部函数中声明定义，然后在通过在函数中定义函数来对他们进行访问操作，这样对外部暴露的是特定的接口，而不是直接访问，起到了很好的封装作用。
```
// 构建一个父对象模块，并用闭包隐藏传递的参数从而形成私有变量
var parent = function (spec){
	var that = {};
    that.getName = function () { // 构造闭包
    	return spec.name;
    };
};

// 构建儿子模块，继承父亲
var child = function (spec){
	var that = parent(spec); // 构建父亲对象
    that.add = function(){ // 差异化继承，拓展自己的接口
    	...
    };
};

var c = child({name: 'test'});
c.getName(); // 就从这里的接口来看，name属性只能访问而不能被修改，相当于私有化了
```
这样来看，通过函数包裹，可以实现对象变量的私有化，如此就能更加愉快地使用js原型继承来写出很多漂亮的代码啦。

以上便是我从阅读《javascript语言精粹》中总结的自己关于原型继承的认识，如果有误还望指出，谢谢，也希望能帮到和我一样的初学者。