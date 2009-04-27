# -*- coding: utf-8 -*-
import locale
from django import forms
from django.contrib.auth.models import User
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
                return u"%s %s" % tuple(data_list)
            except:
                raise forms.ValidationError(ERROR_INVALID)
        return None

GENDERS = (
('M','Male'),
('F','Female')
)        

TOBACCOS = (
(-1, 'Never'),
(5, 'None in last 5 years'),
(4, 'None in last 4 years'),
(3, 'None in last 3 years'),
(2, 'None in last 2 years'),
(1, 'None in last 1 year'),
(0, 'Current User'),
)

RATINGS = (
(4, 'Preferred Plus'),
(3, 'Preferred'),
(2, 'Standard Plus'),
(1, 'Standard'),
)


#(start,stop,step)
COVERAGE_RANGE_DIST = [
(25000,   500001,   25000),
(500000,  1000000,  100000),
(1000000, 5000001,  250000),
(5000000, 10000001, 1000000),
]

COVERAGE_RANGES = []
for r in COVERAGE_RANGE_DIST:
    COVERAGE_RANGES.extend(
        #map(lambda x: (x,locale.currency(x, grouping=True)[:-3]),xrange(*r)))
        # App engine doesnt support locales
        map(lambda x: (x,"$%d" % x), xrange(*r)))

COVERAGE_RANGES = tuple(COVERAGE_RANGES)

TERM = tuple(map(lambda x: (x, '%s years' % x), (15, 20, 30,)))

PAYMENT_MODES = (
    (1, 'Annual'),
    (2, 'Semi-Annual'),
    (4, 'Quarterly'),
    (12, 'Monthly'),
)

class QuoteRequestForm(forms.ModelForm):
    state = USStateField()
    gender = forms.ChoiceField(choices=GENDERS)
    
    dob = forms.DateField()
    height = HeightField()
    weight = forms.IntegerField()
    
    tobacco = forms.ChoiceField(choices=TOBACCOS)
    rating = forms.ChoiceField(choices=RATINGS)
    
    coverage = forms.ChoiceField(choices=COVERAGE_RANGES)
    term = forms.ChoiceField(choices=TERM)
    
    payment_mode = forms.ChoiceField(choices=PAYMENT_MODES)
    
    class Meta:
        model = QuoteRequest
        fields = ('state','gender','dob','height','weight','tobacco',
            'rating','coverage','term')


