#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'HowToPlayER'
SITENAME = 'HowToPlayER'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Minsk'

DEFAULT_LANG = 'by'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
ROOT = os.path.abspath(os.path.dirname(__file__))
THEME = os.path.join(
    ROOT, 'theme'
)

# TEMPLATE_PAGES = {
#     os.path.join(THEME, '')
# }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
