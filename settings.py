#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings

BLOG_TITLE = getattr(settings, 'FBLOG_BLOG_TITLE', 'Blog')
