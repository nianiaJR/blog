---
title: vue源码-sfc/parser.js
date: 2017-03-16
categories: Work
tags: vue
toc: true
---
### 版本2.2.1
### parseComponent
解析sfc的，即单文件组件.vue文件，具体代码还在看，行数不多，但逻辑蛮多的。

```
/* @flow */ 一个静态检查插件，用以进行类型定义检查


import deindent from 'de-indent' // 移除额外的空格缩进，改为\n的形式
import { parseHTML } from 'compiler/parser/html-parser' // html解析器，抽象出AST
import { makeMap } from 'shared/util' // 之前看的关于vue的工具函数

const splitRE = /\r?\n/g // 匹配换行的表达式
const isSpecialTag = makeMap('script,style,template', true) // 创建一个查询字典，用于标记特殊的tag

type Attribute = { // 定义一个类型
  name: string,
  value: string
};

/**
 * Parse a single-file component (*.vue) file into an SFC Descriptor Object.
 */
export function parseComponent (
  content: string,
  options?: Object = {}
 ): SFCDescriptor {
  const sfc: SFCDescriptor = {
    template: null,
    script: null,
    styles: [],
    customBlocks: []
  }
  let depth = 0
  let currentBlock: ?(SFCBlock | SFCCustomBlock) = null

  function start (
    tag: string,
    attrs: Array<Attribute>,
    unary: boolean,
    start: number,
    end: number
  ) {
    if (depth === 0) {
      currentBlock = {
        type: tag,
        content: '',
        start: end,
        attrs: attrs.reduce((cumulated, { name, value }) => {
          cumulated[name] = value || true
          return cumulated
        }, Object.create(null))
      }
      if (isSpecialTag(tag)) {
        checkAttrs(currentBlock, attrs)
        if (tag === 'style') {
          sfc.styles.push(currentBlock)
        } else {
          sfc[tag] = currentBlock
        }
      } else { // custom blocks
        sfc.customBlocks.push(currentBlock)
      }
    }
    if (!unary) {
      depth++
    }
  }

  function checkAttrs (block: SFCBlock, attrs: Array<Attribute>) {
    for (let i = 0; i < attrs.length; i++) {
      const attr = attrs[i]
      if (attr.name === 'lang') {
        block.lang = attr.value
      }
      if (attr.name === 'scoped') {
        block.scoped = true
      }
      if (attr.name === 'module') {
        block.module = attr.value || true
      }
      if (attr.name === 'src') {
        block.src = attr.value
      }
    }
  }

  function end (tag: string, start: number, end: number) {
    if (depth === 1 && currentBlock) {
      currentBlock.end = start
      let text = deindent(content.slice(currentBlock.start, currentBlock.end))
      // pad content so that linters and pre-processors can output correct
      // line numbers in errors and warnings
      if (currentBlock.type !== 'template' && options.pad) {
        text = padContent(currentBlock) + text
      }
      currentBlock.content = text
      currentBlock = null
    }
    depth--
  }

  function padContent (block: SFCBlock | SFCCustomBlock) {
    const offset = content.slice(0, block.start).split(splitRE).length
    const padChar = block.type === 'script' && !block.lang
      ? '//\n'
      : '\n'
    return Array(offset).join(padChar)
  }

  parseHTML(content, {
    start,
    end
  })

  return sfc
}

```