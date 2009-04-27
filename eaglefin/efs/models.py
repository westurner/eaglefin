# -*- coding: utf-8 -*-
from django.db.models import permalink, signals
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db



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

TERMS = tuple(map(lambda x: (x, '%s years' % x), (15, 20, 30,)))

PAYMENT_MODES = (
    (1, 'Annual'),
    (2, 'Semi-Annual'),
    (4, 'Quarterly'),
    (12, 'Monthly'),
)

strip = lambda y: map(lambda x: x[1], y)
stri = lambda y: map(lambda x: x[0], y)

class QuoteRequest(db.Model):
    """Quote request profile with user information"""
    state = db.StringProperty(required=True)
    gender = db.StringProperty(required=True,choices=strip(GENDERS))
    dob = db.DateProperty(required=True,verbose_name="Born on")
    
    height = db.StringProperty(required=True)
    weight = db.IntegerProperty(required=True)
    
    tobacco = db.StringProperty(required=True,choices=strip(TOBACCOS))
    rating = db.StringProperty(required=True,choices=strip(RATINGS))
    
    coverage = db.IntegerProperty(required=True,choices=stri(COVERAGE_RANGES))
    term = db.IntegerProperty(required=True,choices=stri(TERMS), verbose_name="Term (years)")
    
    payment_mode = db.StringProperty(required=True,choices=strip(PAYMENT_MODES))
    
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    def __unicode__(self):
        return "%s %s %s %s" % (self.created, self.state, self.gender, self.dob)
        
    @permalink
    def get_absolute_url(self):
        return ('efs.views.quote_request_detail', (), {'key': self.key()})
