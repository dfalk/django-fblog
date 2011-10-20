#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from fblog.models import Entry

class EntryAdminForm(forms.ModelForm):
    #content = forms.CharField() # override widget

    class Meta:
        model = Entry
        exclude = ('author')

    def __init__(self, *args, **kwargs):
        super(EntryAdminForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['style'] = 'width: 98%'
        self.fields['title'].widget.attrs['style'] = 'width: 98%'
        self.fields['slug'].widget.attrs['style'] = 'width: 98%'
        self.fields['content'].widget.attrs['cols'] = 80
        self.fields['content'].widget.attrs['rows'] = 16
        self.fields['content'].widget.attrs['style'] = 'width: 98%'
        self.fields['related_entries'].widget.attrs['style'] = 'width: 98%'


