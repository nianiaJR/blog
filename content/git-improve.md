Title: Git-日常使用积累
Date: 2015-7-16
Category: Tool
Tags: 2015, summary
Slug: git-improve

### 前言
每天都会用到git，通常来说无外乎是`git commit` `git add` `git checkout`等比较常见的命令，但有时候会遇见遇见一些特殊的情况，一遇见特殊情况每次都需要搜一下git的相关命令，久而久之我觉得搜一次就积累记录一下，成为了很自然而然的事，方便以后自己查看，同时如果能帮到他人那再好不过了。

### 情景

先推荐几个命令缩写，个人感觉很好用
```
git config alias.ci --global commit
git config alias.co --global checkout
git config alias.st --global status
git config alias.br --global branch
```

删除本地冗余commit:
```
// 适用于删除冗余git log
git reset --soft HEAD~[number] //可以回退到历史中的某一次提交，并将后面的修改，添加到工作区域，方便继续提交或者删除修改
git reset --hard HEAD~[number] //这个的效果和上面类似，不过往后的修改就不再暂存了，所以要小心，多数时候用前者就好
```

比较历史log
```
git diff ID1 ID2
```

交互提交到工作区
```
git add -p //这个命令能让你一点一点地review你的修改，并且帮你add
```

补充vim编辑器对git的支持：
```
git commit --amend //失败并报错》error: There is a problem with editor 'vi'
echo export EDITOR=vim >> ~/.zshrc //如果追加到你对应的shell rc文件
```

对于暂存stash的记忆：
```
git stash //保存当前状态，推到一个栈中，并清空暂存区
git stash list //可以看见你的暂存列表
git stash pop //弹出最近一次暂存的修改纪录
git stash apply stash@{[number]} //弹出栈中的对应序列号的暂存内容
```

修改前一次commit的author，有这样的需求往往是你误将自己的个人账户对公司的代码做了提交，这样无法更新到远程库。
```
// 一个命令就可以搞定
git commit --amend --author "New-Auth-Name <emial@address.com>
```