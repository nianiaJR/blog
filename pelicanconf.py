#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'niania'
SITENAME = u'niania正在路上'
SITEURL = 'www.liangjiarui.com'

GITHUB_URL = 'https://github.com/nianiaJR'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

GOOGLE_ANALYTICS = 'UA-60523578-1'

DEFAULT_LANG = u'zh'

THEME='niania_theme'
#THEME='pelican-themes/bootstrap2'

PLUGIN_PATHS = [u"pelican-plugins"]
PLUGINS = ["sitemap"]
SITEMAP = {
        "format": "xml",
        "priorities": {
            "articles": 0.7,
            "indexes": 0.5,
            "pages": 0.3,
         },
        "changefreqs": {
            "articles": "monthly",
            "indexes": "daily",
            "pages": "monthly",
        }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Google', 'https://www.google.com/?gws_rd=ssl'),
         ('OverFlow', 'http://stackoverflow.com/'),
         ('Pelican', 'http://getpelican.com/'),
        )

# Social widget
SOCIAL = (
          ('Github', 'https://github.com/nianiaJR'),
          ('Linkedin', 'http://www.linkedin.com/profile/view?id=406308893'),
          ('Facebook', 'https://www.facebook.com/profile.php?id=100005396027984'),
          (u'豆瓣', 'http://www.douban.com/people/nianiazone/'),
          (u'知乎', 'http://www.zhihu.com/people/nia-nia-83'),
          (u'微博', 'http://weibo.com/p/1005052281074044/home?from=page_100505&mod=TAB#place'),
          ('CSDN', 'http://blog.csdn.net/liangjiaruifighting'),
          ('V2EX', 'http://v2ex.com/member/niania')
         )

FLinks = (
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
