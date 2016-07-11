Title: 创建一个对象的几种方法
Date: 2015-9-05
Category: JavaScript
Tags: 2015, summary
Slug: create-object

### 前言
javascript里经常会需要创建一个对象，但不同的方式创建的对象，是不太一样的。大致的创建方法分为：1.利用Object()来构造、2.利用对象字面量构造、3.利用构造函数来创建对象。在这三个的基础上，又会有一些变化，这里不一一例举了。

### 代码解析
一. 使用Object()
```
/*
 * 通过new Object()来创建一个实例
 */
(function test1() {
    console.log("这是通过new Object来创建的对象");
    var person = new Object();
    person.name = 'test1';
    person.sayName = function() {
        console.log(this.name);
    };

    console.log(person);
    person.sayName();
})();
```

二. 使用对象字面量
```
/*
 * 通过对象字面量
 */
(function test2(){
    console.log("这是通过字面量来创建的对象")
    var person = {
        name: 'test2',
        sayName: function() {
            console.log(this.name);
        }
    };
    console.log(person);
    person.sayName();
})();
```

三. 工厂模式
```
/*
 * 工厂模式创建对象：其实不过是为了解决创建同一类型对象的时候，封装成函数，这样
 * 少写一些代码
 * 注意：工厂模式虽然解决了重复构造对象代码重用问题，不过不能判断一个对象的类型
 */
(function test3(){
    console.log("这是通过工厂模式创建的对象")
    function createPerson(name) {
        var o = new Object();
        o.name = name;
        o.sayName = function() {
            alert(this.name);
        };
        return o;
    }
    var p1 = createPerson('testp1');
    var p2 = createPerson('testp2');
    console.log("p1", p1);
    console.log("p2", p2);
})();
```

四. 构造函数
```
/*
 * 通过构造函数，可以既解决对象识别，又可以解决代码重用问题
 * 通过new操作符，构造函数会经历4个过程：
 * 1、创建一个新对象
 * 2、将构造函数的作用域赋值给新对象
 * 3、执行构造函数的代码
 * 4、返回新对象
 */
(function test4(){
    console.log('这是构造函数创建对象');
    function Person(name) {
        this.name = name;
        this.sayName = function() {
            alert(this.name);
        };
    }
    var p1 = new Person('test1');
    var p2 = new Person('test2');
    console.log('p1>>>>>', p1);
    console.log('p2>>>>>', p2)
    // 通过构造函数创建的对象，他们的constructor属性指向的是创建他们的构造函数
    console.log('p1的构造函数是', p1.constructor);
    console.log('p2的构造函数是', p2.constructor);
    // instanceof操作符也可以用来判断对象实例是否属于某一对象类型
    console.log(p1 instanceof Person);
    console.log(p2 instanceof Person);
    console.log('p1,p2的函数实例一样么：', p1.sayName == p2.sayName);

    // 这个构造函数存在的问题是，每次新new一个对象，都会产生一个新的函数实例，
    // 但这些函数又执行相同的功能，造成浪费。
})();
/*
 * 解决函数实例不同这个问题，可以通过prototype来实现, 每当构造函数构造一个对象后
 * 该实例对象就会继承这个原型对象
 */
(function test5(){
    console.log('这是构造函数创建对象, 但函数方法被写到了原型上');
    function Person(name) {
        this.name = name;
    }

    Person.prototype.sayName = function() {
        alert(this.name);
    };

    var p1 = new Person('test1');
    var p2 = new Person('test2');
    console.log('p1>>>>>', p1);
    console.log('p2>>>>>', p2)
    // 通过构造函数创建的对象，他们的constructor属性指向的是创建他们的构造函数
    console.log('p1的构造函数是', p1.constructor);
    console.log('p2的构造函数是', p2.constructor);
    // instanceof操作符也可以用来判断对象实例是否属于某一对象类型
    console.log(p1 instanceof Person);
    console.log(p2 instanceof Person);

    console.log('p1,p2的函数实例一样么：', p1.sayName == p2.sayName);
})();
```

五. 组合使用构造函数模式和原型模式
```
/*
 * 这样的需求主要缘于原型模式共享的本性所导致的，原型中所有的属性是被很多实例所共享的，
 * 尤其对于引用类型，一旦其一个实例更改了原型中的引用类型，那在其他实例里也会反映出来。
 * 由此便出现了构造函数模式和原型模式组合的使用：
 * 构造函数用于定义实例属性，而原型模式用于定义方法和共享属性。
 */
// 构造函数创建实例属性
function Person(name, age, job) {
	this.name = name;
    this.age = age;
    this.job = job;
    this.friends = ['Shelby', 'Court'];
}
// 原型定义方法和共享的属性
Person.prototype = {
	constructor: Person,
    sayName: function(){
    	alert(this.name);
    }
};
// Test:
var p1 = new Person('Nicholas', 29, 'Software Engineer');
var p2 = new Person('Greg', 27, 'Doctor');
p1.friends.push('van');
alert(p1.friends); // 'Shelby, Count, Van'
alert(p2.friends); // 'Shelby, Count' 不会再出现共享引用对象而导致的问题了
alert(p1.friends === p2.friends); // false, 每个实例都会有自己的一份实力属性的副本
alert(p1.sayName === p2.sayName); // true, 但实例间的方法依然是共享的
```

