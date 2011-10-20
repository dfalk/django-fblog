#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db.models import get_model
from django.template import Library, Node
from django.template import TemplateSyntaxError
from django.contrib.sites.models import Site
from fblog.models import Entry, EntryCategory
from django.utils.translation import ugettext as _
import calendar

register = Library()

@register.filter()
def cut(text):
    """
    Cut text
    @return text before <!-- cut --> tag
    >>> cut("desctiption<!-- cut -->text")
    'desctiption'
    >>> cut("description text")
    'description text'
    """
    return text.split('<!-- cut -->')[0]

@register.filter
def month_name(month_number):
    return _(calendar.month_name[int(month_number)])

@register.inclusion_tag('fblog/category_menu.html')
def category_menu():
    category_menu = EntryCategory.objects.all()
    return {'category_menu': category_menu}

@register.inclusion_tag('fblog/archive_monthes.html')
def archive_monthes():
    blog_month_list = Entry.objects.dates('publish','month',order='DESC')
    return {'blog_month_list': blog_month_list}

@register.inclusion_tag('fblog/archive_tree.html')
def archive_tree(current_entry=None):
    entry_list = Entry.objects.published()
    current_entry = current_entry
    return {'entry_list': entry_list, 'current_entry': current_entry}

@register.inclusion_tag('fblog/latest_menu.html')
def latest_menu(num=5,featured=""):
    if featured == "featured":
        entry_list = Entry.objects.published().filter(is_featured=True)[:num]
    else:
        entry_list = Entry.objects.published()[:num]
    return {'entry_list': entry_list}


class LatestContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))
        
    def render(self, context):
        site = Site.objects.get_current()
        context[self.varname] = self.model._default_manager.published()[:self.num]
        return ''

def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])
get_latest = register.tag(get_latest)


class LatestFeaturedContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))
        
    def render(self, context):
        site = Site.objects.get_current()
        context[self.varname] = self.model._default_manager.published().filter(is_featured=True)[:self.num]
        return ''

def get_latest_featured(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest_featured tag must be 'as'"
    return LatestFeaturedContentNode(bits[1], bits[2], bits[4])
get_latest_featured = register.tag(get_latest_featured)
