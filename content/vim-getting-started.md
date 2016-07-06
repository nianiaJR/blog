Title: 新手使用vim心得
Date: 2015-5-1
Category: Work
Tags: 2015, summary, vim
Slug: vim-getting-started

## 前言

之前用了一段时间vim，不过当时还是偏向于sublime，现在因为实习任务不那么重了，加上vim下的酷黑编辑区以及裂屏十分吸引人，所以又开始尝试去使用vim了，以前听别人说过一句话，表示很赞同，vim是用出来的，不是学出来的，没必要非要看书学习，看够了才去使用，你更应该的是边用边学，在使用的过程中，要多想想我需要它有哪些功能，然后打开google一下，说不定又能发现一个新的插件，使得你的vim更加便捷，下面是我作为一个新人，这一个月使用vim总结的一些经验，希望与各位初学者一起分享～
![vim1.png](http://7xja3v.com1.z0.glb.clouddn.com/vim1%20%281%29.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:b8jG5O9-fBmdX20TUwJdNQM945I)

## 关键词 (方便直接google学习的同学)

Vundle NERDTree Ag IndentLine quickfix tab mark vim－mode VimL vim-map vim-shortcut

## 插件推荐

使用vim必须得使用插件，不然很难用，一旦有了插件，vim的强大就开始了。

### 为了省事方便，我是将所有vim配置写在根目录下的~/.vimrc里面的，所以后面的配置以及下载都是写在此文件中。

### vundle-插件管理工具

[https://github.com/gmarik/Vundle.vim](https://github.com/gmarik/Vundle.vim) 负责下载插件，删除插件用的，每次下插件只需要到对应的vimrc文件里面写上Plugin 'xxx'，然后运行命令:PluginInstall就能直接下载插件了,具体请看vundle的README。

![vim2.png](http://7xja3v.com1.z0.glb.clouddn.com/vim2.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:FQyiWPBTiV6kEoMaEGVIEqL6TxM)
### NERDTree-树形目录结构（就像上图左侧那样）

[https://github.com/scrooloose/nerdtree](https://github.com/scrooloose/nerdtree) 使用命令: ":NERDTree"![vim3.png](http://7xja3v.com1.z0.glb.clouddn.com/vim3.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:oA0wxNNGhWmgtCTejnhNC8HaYyg)

### 颜色配置

![vim4.png](http://7xja3v.com1.z0.glb.clouddn.com/vim4.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:CF-RnQhWris54wCGqvgMe06Ea_k)
### IndentLine-缩进线条提示

[https://github.com/Yggdroot/indentLine](https://github.com/Yggdroot/indentLine)

![vim6.png](http://7xja3v.com1.z0.glb.clouddn.com/vim6.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:PdKoC9KhO4NArNZjLRXGtruZR5o)
### Ag-快速查找工具（比grep快很多）

[https://github.com/ggreer/the_silver_searcher](https://github.com/ggreer/the_silver_searcher)

![vim7.png](http://7xja3v.com1.z0.glb.clouddn.com/vim7.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:1pAkMHI6FPkY_jLGBueg2R4eMCk)
使用：":Ag xxx" －在当前目录下查找xxx，后面也可以＋目录，具体看: Ag - h 查询的结果会显示在quickfix里面：

![vim8.png](http://7xja3v.com1.z0.glb.clouddn.com/vim8.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:SEXYKOWQpoOIXVPDcvZsSx-M8YQ)
这样只要在quickfix里面浏览查找结果，编辑区就会自动跳到那个匹配的文件

_由于插件太多，只要多去思考需求，然后google，就能发现更多好用的插件_

## 常用命令 + 默认快捷键

h,j,k,l－－尽量不要用右下的方向键，因为后面会感觉慢的 NERDTreeFind －－找出当前文件位于NERDTree目录结构中的位置，游标会移动到那 copen－－打开 quickfix窗口 cclose－－关闭

Ag xxx －－查找xxx _quickfix打开的情况下_ cp －－移动到上一个匹配文件 cn －－移动到下一个匹配文件

tabnew －－ 新开一个tab标签页 tabn －－ 移动到下一个标签页 tabp －－ 移动到上一个标签页

mark a 标记当前行 `a 跳到标记处

vsplit －－纵向裂屏 split －－横向裂屏 Ctr + w －－光标在各个分配之间切换 Ctr + w + h/j/k/l －－让光标的切换具有方向性

### 光标移动

w －－按单词向后移动 b －－按单词向前移动 $ －－跳到行尾 0 －－跳到行首 G －－移动到文件末尾 H －－移动到文件头 ctr + u 向上翻页 ctr + d 向下翻页

### 修改文件

d+w －－按单词删除 o -－向下打开一个新行 O －－向上打开一个新行 :%s/xxx/yyy/gc －－把xxx换成yyy d+d 删除当前行 n + dd 删除n行 yy －－复制当前行 v －－进入视图选择

### 大部分命令常用命令一般都会配置成快捷键的，这样使用起来特别方便

![vim10.png](http://7xja3v.com1.z0.glb.clouddn.com/vim10.png?attname=&e=1432831561&token=6kI_1mWJ6jEyr5-1PmIcvgX2Y01gJ83Pdf9A1hQ1:DFBMlhZpZ-jT50SsGPYJJh8Ly5w)
这里按Shift+l就相当于之前的tabn了

大部分小结内容就在这了，如果有兴趣且不嫌弃可以看我的vimrc配置:[https://github.com/nianiaJR/Jerry-vimrc](https://github.com/nianiaJR/Jerry-vimrc)
