#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from fblog.models import Entry

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Entry.objects.published()

    def lastmod(self, obj):
        return obj.date_publish
