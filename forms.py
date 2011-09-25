#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from fblog.models import Entry

class EntryAdminForm(forms.ModelForm):
    #content = forms.CharField() # override widget

    class Meta:
        model = Entry
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super(EntryAdminForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['cols'] = 80
        self.fields['content'].widget.attrs['rows'] = 20
        self.fields['preview'].widget.attrs['cols'] = 80

