#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import url, patterns
from fblog.feeds import BlogFeed

urlpatterns = patterns('fblog.views',

    # List views
    url(r'^$', view='entry_list', name='blog_index'),
    url(r'^rss/$',
        view=BlogFeed(),
        name='blog_rss'
    ),

    # Entry views
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        view='entry_detail',
        name='blog_entry_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/edit/$',
        view='entry_edit',
        name='blog_entry_edit'
    ),
    url(r'^new/$',
        view='entry_new',
        name='blog_entry_new'
    ),

    # Piblishing views
    url(r'^publishing/$',
        view='entry_publishing',
        name='blog_publishing'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/publish/$',
        view='entry_publish',
        name='blog_entry_publish'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/hide/$',
        view='entry_hide',
        name='blog_entry_hide'
    ),

    # Additional views
    url(r'^category/(?P<slug>[-\w]+)/$',
        view='category_detail',
        name='blog_category_detail'
    ),
    url(r'^(?P<year>\d{4})/$',
        view='entry_archive_year',
        name='blog_archive_year'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        view='entry_archive_month',
        name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        view='entry_archive_day',
        name='blog_archive_day'
    ),
)

