#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, time
from django.views.generic import date_based, list_detail
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.utils import simplejson
from fblog.models import Entry, EntryCategory
from fblog.forms import EntryAdminForm

def entry_list(request, page=0, template_name='fblog/entry_list.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Entry.objects.published(),
        paginate_by = 10,
        page = page,
        template_name = template_name,
        **kwargs)

def entry_detail(request, year, month, day, slug, **kwargs):
    entry = Entry.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=slug)
    return direct_to_template(request,'fblog/entry_detail.html', {'entry': entry})

@permission_required('fblog.change_entry')
def entry_publish(request, year, month, day, slug, **kwargs):
    entry = Entry.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=slug)
    entry.is_published = True
    entry.save()
    if request.is_ajax():
        data = "public"
        return HttpResponse(data)
    else:
        return HttpResponseRedirect(entry.get_absolute_url())

@permission_required('fblog.change_entry')
def entry_hide(request, year, month, day, slug, **kwargs):
    entry = Entry.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=slug)
    entry.is_published = False
    entry.save()
    if request.is_ajax():
        data = "hidden"
        return HttpResponse(data)
    else:
        return HttpResponseRedirect(entry.get_absolute_url())

@permission_required('fblog.change_entry')
def entry_publishing(request, page=0, template_name='fblog/entry_publishing.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Entry.objects.filter(is_published=False),
        paginate_by = 10,
        page = page,
        template_name = template_name,
        **kwargs)

@permission_required('fblog.add_entry')
def entry_new(request, **kwargs):
    if request.method == 'POST':
        form = EntryAdminForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.author = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('blog_index'))
    else:
        form = EntryAdminForm()

    return direct_to_template(request, 'fblog/entry_new.html',{'form':form})

@permission_required('fblog.change_entry')
def entry_edit(request, year, month, day, slug, **kwargs):
    entry = Entry.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=slug)
    if request.method == 'POST':
        form = EntryAdminForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(entry.get_absolute_url())
    else:
        form = EntryAdminForm(instance=entry)

    return direct_to_template(request, 'fblog/entry_edit.html',{'form':form,'entry':entry})

def category_detail(request, slug, **kwargs):
    category_list = Entry.objects.filter(category__slug__exact=slug)
    category = EntryCategory.objects.get(slug=slug)
    return direct_to_template(request,'fblog/category_detail.html', {'object_list': category_list, 'category': category })

def entry_archive_year(request, year, page=0, template_name='fblog/entry_archive_year.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Entry.objects.published().filter(publish__year=year),
        paginate_by = 10,
        page = page,
        template_name = template_name,
        extra_context = {'year':year},
        **kwargs)

def entry_archive_month(request, year, month, page=0, template_name='fblog/entry_archive_month.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Entry.objects.published().filter(publish__year=year, publish__month=month),
        paginate_by = 10,
        page = page,
        template_name = template_name,
        extra_context = {'month':datetime.date(int(year),int(month),1)},
        **kwargs)

def entry_archive_day(request, year, month, day, page=0, template_name='fblog/entry_archive_day.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Entry.objects.published().filter(publish__year=year, publish__month=month, publish__day=day),
        paginate_by = 10,
        page = page,
        template_name = template_name,
        extra_context = {'day':datetime.date(int(year),int(month),int(day))},
        **kwargs)

