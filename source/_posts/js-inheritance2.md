---
title: 第二次总结－javascript原型继承的几种写法
date: 2015-9-06
categories: JavaScript
tags: 原型继承
---

### 前言
上次面试被问到javascript有几种继承方式的时候，虽然上次看蝴蝶书的时候也做了一次小结，但并不完备，缺少了最常用的继承方式记录，答得很糟糕，这次一并做一次总结，希望那种事不要再发生了。

### 原型继承
一. 普通继承
```
// 定义父类构造函数
function SuperType(){
	this.property = true;
};
// 父类的原型方法
SuperType.prototype.getSuperValue = function(){
	return this.property;
};
function SubType(){
	this.subproperty = false;
}
// 通过改变子类的原型对象来实现继承，将子类的原型对象赋值为父类的一个实例对象即可
SubType.prototype = new SuperType();
// 可以继续在自己的原型上继续扩展，继续为那个实例对象添加方法
SubType.prototype.getSubValue = function (){
	return this.subproperty;
};
var instance = new SubType();
alert(instance.getSuperValue()); // true, 使用了继承来的原型方法
```
<p style="color: red">缺点：由于子类的原型是另一个类型（父类）的实例，如果该实例中含有“引用”类型值，那么引用类型的原型属性会被所有实例所共享，大多数时候，这并不是一个好主意。</p>

```
// 共享引用类型的原型实例
function SuperType(){
	// 即将作为原型对象上的引用类型属性
	this.colors = ["red", "blue", "green"];
}
function SubType(){
}
SubType.prototype = new SuperType();
var instance1 = new SubType();
instance1.colors.push("black");
alert(instance1.colors);     // "red,blue,green,black"
var instance2 = new SubType();
alert(instance2.colors);     // "red,blue,green,black" 原型对象的被改了，即共享了。
```

二. 借用构造函数的继承
```
function SuperType(){
	this.colors = ["red", "blue", "green"];
}
function SubType() {
	// 通过call来委托，继承SuperType，起到拷贝引用属性副本的效果
    SuperType.call(this);
}
var instance1 = new SubType();
instance1.colors.push("black");
alert(instance1.colors); // "red, blue, green, black"
var instance2 = new SubType();
alert(instance2.colors); // "red, blue, green" 这就不再会存在共享引用属性的问题了，关键在于call和new的作用。
```
<p style="color: red;">缺点：假如方法均在构造函数中定义，那么函数复用就失去意义了，所以构造函数模式一般不单独使用。</p>

三. 组合继承
指的是将原型链和借用构造函数的技术组合到一块，发挥二者各自特点的继承模式。
```
function SuperType(name) {
	this.name = name;
    this.colors = ["red", "blue", "green"];
}
SuperType.prototype.sayName = function(){
	alert(this.name);
};
function SubType(name, age){
	// 这里依旧使用借助call来实现继承，copy引用类型值副本，避免共享
    SuperType.call(this, name);
    this.age = age;
}
// 这里使用原型继承方式，使得方法被复用，总之为了继承方法
SubType.prototype = new SuperType();
SubType.prototype.constructor = SubType;
// 扩展继承的原型对象的方法
SubType.prototype.sayAge = function(){
	alert(this.age);
};
// 测试效果：
var instance1 = new SubType('T1', 29);
instance1.colors.push('black');
alert(instance1.colors); // 'red, blue, green, black'
instance1.sayName(); // 'T1'
instance1.sayAge(); // 29
var instance2 = new SubType('T2', 30);
alert(instance2.colors); //'red, blue, green' 并未共享引用类型属性
instance2.sayName();   // 'T2'
instance2.sayAge();	   // 30
```
<p style="color: red;">组合继承避免了原型链和借用构造函数的缺陷，融合了两者优点，是最常用的一种继承模式（我上次面美团就栽在这里了，其实之前也看过不少遍，就是缺乏实践和总结，下次别踩了），不过这种模式也会稍稍有点点瑕疵，就是同样引用类型属性会同时存在于实例属于和原型属性上，一次来源于call委托生成的位于实例对象上，一个是由于原型继承后，原型对象自带的。</p>

四. 原型继承
通过使用Object.create的方式来避免使用构造函数，实现一种“轻量级”的原型继承
```
var person1 = {
	name: 'T1',
    friends: ['a', 'b', 'c']
};
var person2 = Object.create(person1); // 通过Object.create方法来“浅”复制对象
person2.name = 'T2';
person2.push('d');
var person3 = Object.create(person1);
person3.name = 'T3';
person3.push('e');
alert(person.friends); // 'a, b, c, d, e'
```
<p style="color: red">采用这种方法避免了建立构造函数来实现继承的麻烦，对于只想让一个对象与另一个对象保持类似的情况还是很受用的。不过一定要记住，这里的引用类型值是共享的。</p>

五. 寄生组合式继承
就像前面说的，常用的组合继承，会存在相同属性同时存在于原型对象和实例对象上的情况，主要是因为无论什么情况下，组合继承都会调用两次父类型构造函数：一次在原型上，一次在子类型构造函数内部，所以才导致了重复存在的问题。
```
function inheritPrototype(subType, superType){
	var prototype = Object.create(superType.prototype); // 这样只会浅复制原型上的方法，而不会想构造函数那样带上函数内部生成的属性，这里是关键。
    prototype.constructor = subType; // 弥足指向正确的构造函数
    subType.prototype = prototype;  // 指定对象继承；
}
// 继续组合继承
function SuperType(name){
	this.name = name;
    this.colors = ["red", "blue", "green"];
}
SuperType.prototype.sayName = function(){
	alert(this.name);
};
function SubType(name, age){
	SuperType.call(this, name);
    this.age = age;
}
inheritPrototype(SubType, SuperType);
SubType.prototype.sayAge = function(){
	alert(this.age);
};
var instance = new SubType('T1', 19); // 这样只会使用一次new 构造函数，另一次被“浅复制”替代，避免了没必要属性的定义。
```

<p style="color: red;">以上便是javascript常见的继承模式，希望有用，好坑不踩第二次</p>
