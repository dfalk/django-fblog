#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from fblog import settings
from django.core.urlresolvers import reverse
from fblog.models import Entry

class BlogFeed(Feed):
    title_template = 'feeds/entry_title.html'
    description_template = 'feeds/entry_description.html'

    title = settings.BLOG_TITLE
    description = 'Latest Blog Entries'

    def link(self):
        return reverse('blog_index')

    def items(self):
        return Entry.objects.published()[:10]

    def item_pubdate(self, item):
        return item.date_publish

