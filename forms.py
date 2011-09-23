#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from fblog.models import Entry

class EntryAdminForm(forms.ModelForm):
    #content = forms.CharField() # override widget

    class Meta:
        model = Entry
        exclude = ('author',)
