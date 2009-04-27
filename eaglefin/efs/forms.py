# -*- coding: utf-8 -*-
import locale
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.core.files.uploadedfile import UploadedFile
from django.utils.translation import ugettext_lazy as _, ugettext as __

from ragendja.auth.models import UserTraits
from ragendja.forms import FormWithSets, FormSetField

from django.contrib.localflavor.us.forms import USStateField, USStateSelect

from efs.models import QuoteRequest

#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
#conv = locale.localeconv()


class HeightWidget(forms.MultiWidget):
    def __init__(self, *args, **kwargs):
        feet = map(lambda x: (x,x), xrange(0,9))
        inches = map(lambda x: (x,x), xrange(0,13))
        
        widgets = (
            forms.Select(choices=feet),
            forms.Select(choices=inches),
        )
        super(HeightWidget, self).__init__(widgets, *args, **kwargs)
        
    def format_output(self, widgets):
        return u'''%s Feet %s Inches''' % tuple(widgets)
        
    def decompress(self, value):
        if value:
            return (value.split(' '))
        return (None, None,)
        
class HeightField(forms.MultiValueField):
    widget = HeightWidget
    def __init__(self,*args,**kwargs):
        fields = (
            forms.IntegerField(required=True),
            forms.IntegerField(required=True)
        )
        super(HeightField, self).__init__(fields, *args, **kwargs)
        
    def compress(self, data_list):
        EMPTY_VALUES = (None, '',)
        ERROR_EMPTY = "Please enter your height"
        ERROR_INVALID = "Please enter valid height"
        
        if data_list:
            if filter(lambda x: x in EMPTY_VALUES, data_list):
                raise forms.ValidationError(ERROR_EMPTY)
            try:
                return u'''%s %s''' % tuple(data_list)
            except:
                raise forms.ValidationError(ERROR_INVALID)
        return None



class QuoteRequestForm(forms.ModelForm):
    state = forms.CharField(widget=USStateSelect)

    
    dob = forms.DateField(widget=AdminDateWidget, label="Born on")
    height = HeightField()
    weight = forms.IntegerField()
    

    
    class Meta:
        model = QuoteRequest
        fields = ('state','gender','dob','height','weight','tobacco',
            'rating','coverage','term','payment_mode')


