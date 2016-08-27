---
title: highcarts 改写tooltip.formatter心得
date: 2016-07-14
categories: Work
tags: Highcharts
---

### 前言
应郭老板需求，修改面积area图的tooltip显示，让它既能显示数值比，又能显示百分比，就像做完的时候这样（这个tooltip是我修改过的）：
![tooltip](http://7xja3v.com1.z0.glb.clouddn.com/highchart-tooltip.png)

### 过程描述
这虽然是一件比较容易的事，在查阅文档后，我知道就是修改 [tooltip](http://www.highcharts.com/docs/chart-concepts/tooltip)，tooltip里面有几个属性：pointFormat、pointHeader、formatter，前两个直接衔接的是html字符串，而且pointFormat指的是一个点，比如列表页uv的html片段，pointHeader指的是前面的日期开头，然后后面它会自动枚举，而最后一个formatter则是包含所有的tooltip内容即header和body具体的可以看文档，而这里我想说的是，原本我以为既然是html片段，那么我把样式内联到里面是自然而然的事，可是不论我怎么设置，这个tooltip的样式根本不由我管理，除了颜色我还能控制下，别的几乎是失效的，这一度让我怀疑是highcharts的bug，所以我就开始懵逼了，就打算寻求帮助，由于数据可视化这块公司基本就我在写，所以可能highcharts还真找不到像我一样经常用的...所以我抖了机灵就去搜highcharts的中文QQ群，遗憾的是高级群我进不去，初级群里面问了一下也没什么人理我...大家都忙着撩妹扯淡，然后懵逼之下，我就严重怀疑这是highcharts的bug，然后自豪地跑去了他的官方github库里面去提issue，当然我怕被嘲笑又先在已有的issue里面查了一下，居然还真让我找到了一个相关的，从描述中我知道了tooltip中还有useHTML这个参数，是个boolean类型，设置为true说明这个tooltip采用的是HTML，默认是false...则采用的Canvas，这下原因就找到了，用的Canvas模式，那CSS能管用么...更改过后果然样式就起作用了，一下子开心的不得了。

### 小小的收获
通过这么一件小事情，我还是有这么一些感悟：
1. Boss提的这个要求还真不错，做完以后我发现确实很有用，这让我觉的自己是应该没事多看看Highcharts的文档，多了解一些每个参数的意义，然后结合pipe来优化数据的可视化，这一点还是很有意义的。
2. 就是遇见的那个奇奇怪怪的问题，这个过程中我对于自己的思考也还算满意的，毕竟我一直在想着解决办法，离一个未知的答案越来越近，虽然这个过程还是有点特别的，比如加那个扯淡的讨论群...我觉得以后应该多模重复这种思考的过程，这样能让我解决问题的能力大大提升。同时这个过程中更效率做法，或许还真是直接去看官方的issue，因为你遇见的奇怪问题，其实大家可能普遍也会遇见，你搜一搜或许就会有惊喜。