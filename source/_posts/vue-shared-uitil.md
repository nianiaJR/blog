---
title: vue源码-shared/util.js
date: 2017-03-16
categories: Work
tags: vue
toc: true
---
### 版本2.2.1
### _toString
可接收任何参数，并转化为字符串，为null转化为空字符串，如果是对象则转化为缩进格式为2的json，其余直接转化为字符串。
```
export function _toString (val: any): string {
  return val == null
    ? ''
    : typeof val === 'object'
      ? JSON.stringify(val, null, 2)
      : String(val)
}
```
ps:
JSON.stringify()函数
1. 平常一般只用传入第一个参数。

2. 第二个参数是replacer: 可传入function来改变stringify的行为，或者传入数组作为白名单来筛选能返回的json。

3. 第三个参数是缩进的参数，代表缩进的空格数。

### toNumber
并无太多特别的，就是注意NaN是number类型的，一旦传入的参数不能返回正常数字，返回原字符串
```
export function toNumber (val: string): number | string {
  const n = parseFloat(val)
  return isNaN(n) ? val : n
}
```

### makeMap
将传入的字符串以逗号拆分为每个key，创建成map，返回一个函数，用以检查传入的key是否在这个map中，同时支持传入第二个参数，以处理key的小写转化处理，这是为后面的功能函数isBuilInTag做铺垫。
```
export function makeMap (
  str: string,
  expectsLowerCase?: boolean
): (key: string) => true | void {
  const map = Object.create(null)
  const list: Array<string> = str.split(',')
  for (let i = 0; i < list.length; i++) {
    map[list[i]] = true
  }
  return expectsLowerCase
    ? val => map[val.toLowerCase()]
    : val => map[val]
}
```

### isBuiltInTag
查询是否为内置标签或属性：
```
export const isBuiltInTag = makeMap('slot,component', true)
```

### remove
移除数组中的匹配该值的第一个元素，如果存在则返回一个数组包含这个被移除的数
```
export function remove (arr: Array<any>, item: any): Array<any> | void {
  if (arr.length) {
    const index = arr.indexOf(item)
    if (index > -1) {
      return arr.splice(index, 1)
    }
  }
}
```

### hasOwn
判断某个属性是否是object的自有属性，调用的还是原型链上的方法。
```
const hasOwnProperty = Object.prototype.hasOwnProperty
export function hasOwn (obj: Object, key: string): boolean {
  return hasOwnProperty.call(obj, key)
}
```

### isPrimitive
判断当前值是不是简单值类型，其实就是判断是不是number或者string
```
export function isPrimitive (value: any): boolean {
  return typeof value === 'string' || typeof value === 'number'
}
```

### cached
创建一个带有缓存功能的function，从功能来说，函数传入前和cached后其实作用一样，这里只是通过闭包实现了把已经计算过的值缓存一下，方便下次使用，用空间换时间。
```
export function cached<F: Function> (fn: F): F {
  const cache = Object.create(null)
  return (function cachedFn (str: string) {
    const hit = cache[str]
    return hit || (cache[str] = fn(str))
  }: any)
}
```
ps:
1. <F: Function>这是一个TypeScript的泛型定义，限定传入的参数是一切函数类型。
2. 用Object.create(null)的方式创建的object，区别与字面量{}的方式，是不具备原型的，比如没有toString这样的方法，这样的创建方式更贴近于字典的简单含义，开销更小。

### camelize
将连字符转化为驼峰的字符串，不过此处使用了之前的功能函数cached，用以缓存已经被计算过的值
ps: replace第二个参数是一个回调函数，第一个参数是匹配字符串，之后的参数依次为捕获的字符串
```
const camelizeRE = /-(\w)/g
export const camelize = cached((str: string): string => {
  return str.replace(camelizeRE, (_, c) => c ? c.toUpperCase() : '')
})
```

### capitalize
将首字母转为大写，很普通的转换方法，不过这里从语言基础上说明js的字符串的值是不可以被改变的，只能重新创建一个字符串
```
export const capitalize = cached((str: string): string => {
  return str.charAt(0).toUpperCase() + str.slice(1)
})
```

### hyphenate
连字符化，replace写两遍的原因在于大写字母连续的情况，比如aHHH转化为a-H-H-H
```
const hyphenateRE = /([^-])([A-Z])/g
export const hyphenate = cached((str: string): string => {
  return str
    .replace(hyphenateRE, '$1-$2')
    .replace(hyphenateRE, '$1-$2')
    .toLowerCase()
})
```
### bind
bind的简单实现，据说比原生实现更快，是因为多了一些判断，少传参数了么？
```
export function bind (fn: Function, ctx: Object): Function {
  function boundFn (a) {
    const l: number = arguments.length
    return l
      ? l > 1
        ? fn.apply(ctx, arguments)
        : fn.call(ctx, a)
      : fn.call(ctx)
  }
  // record original fn length
  boundFn._length = fn.length
  return boundFn
}
```

### toArray
类数组转华为真数组，支持自定义起始下标，不知道类比与slice这样的方式有何特殊的地方？
```
export function toArray (list: any, start?: number): Array<any> {
  start = start || 0
  let i = list.length - start
  const ret: Array<any> = new Array(i)
  while (i--) {
    ret[i] = list[i + start]
  }
  return ret
}
```
### extend
对象拓展，将原对象的引用复制过来进行拓展，注意拓展对象中引用属性对象被改变也会影响原对象
```
export function extend (to: Object, _from: ?Object): Object {
  for (const key in _from) {
    to[key] = _from[key]
  }
  return to
}
```
### isObject
判断是否是一个JSON对象
```
export function isObject (obj: mixed): boolean {
  return obj !== null && typeof obj === 'object'
}
```

### isPlainObject
判断是否是一个普通的js对象，区别于上面的isObject，比如[]这里就是false
```
const toString = Object.prototype.toString
const OBJECT_STRING = '[object Object]'
export function isPlainObject (obj: any): boolean {
  return toString.call(obj) === OBJECT_STRING
}
```

### toObject
把一个对象数组合并成一个单一对象
```
export function toObject (arr: Array<any>): Object {
  const res = {}
  for (let i = 0; i < arr.length; i++) {
    if (arr[i]) {
      extend(res, arr[i])
    }
  }
  return res
}
```

### genStaticKeys
从编译器中生成一个静态字符串密钥，这里还暂时不太能解释这个的作用，待完成。。。
```
export function genStaticKeys (modules: Array<ModuleOptions>): string {
  return modules.reduce((keys, m) => {
    return keys.concat(m.staticKeys || [])
  }, []).join(',')
}
```

### looseEqual
判断两个值是否是普通意义上的值相等，包括对象的比较，如果从表面上的值相当，那就是相等，比如111和'111'相等
```
export function looseEqual (a: mixed, b: mixed): boolean {
  const isObjectA = isObject(a)
  const isObjectB = isObject(b)
  if (isObjectA && isObjectB) {
    return JSON.stringify(a) === JSON.stringify(b)
  } else if (!isObjectA && !isObjectB) {
    return String(a) === String(b)
  } else {
    return false
  }
}
```

### looseIndexOf
有了宽松的相等，这里就是在宽松相等的基础上，找到对应宽松相等的值在数组中的下标
```
export function looseIndexOf (arr: Array<mixed>, val: mixed): number {
  for (let i = 0; i < arr.length; i++) {
    if (looseEqual(arr[i], val)) return i
  }
  return -1
}
```
### once
确保一个函数只执行一次，利用闭包保存状态的特性
```
export function once (fn: Function): Function {
  let called = false
  return () => {
    if (!called) {
      called = true
      fn()
    }
  }
}
```