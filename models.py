#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from fblog.managers import PublicManager
from datetime import datetime

class EntryCategory(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    order = models.PositiveIntegerField('Display Order', blank=True, null=True)

    class Meta:
        ordering = ('order','title')

    def __unicode__(self):
        return u"%s" % (self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('fblog.views.category_detail',[self.slug])

class Entry(models.Model):
    author = models.ForeignKey(User, related_name='author')
    category = models.ForeignKey(EntryCategory, blank=True, null=True)

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique_for_date="date_publish", max_length=100)
    content = models.TextField(help_text="Use <!-- cut --> for split text in list view.")

    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_publish = models.DateTimeField(default=datetime.now)
    related_entries = models.ManyToManyField('self', blank=True, null=True)
    enable_comments = models.BooleanField(default=True)

    objects = PublicManager()

    class Meta:
        ordering = ['-date_publish']
        get_latest_by = 'date_publish'

    def __unicode__(self):
        return u"%s" % (self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('fblog.views.entry_detail', [self.date_publish.year, self.date_publish.strftime("%m"), self.date_publish.strftime("%d"), self.slug])

