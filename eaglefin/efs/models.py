# -*- coding: utf-8 -*-
from django.db.models import permalink, signals
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db

class QuoteRequest(db.Model):
    """Quote request profile with user information"""
    state = db.StringProperty()
    gender = db.StringProperty()
    dob = db.DateProperty()
    
    height = db.StringProperty()
    weight = db.IntegerProperty()
    
    tobacco = db.IntegerProperty()
    rating = db.StringProperty()
    
    coverage = db.IntegerProperty()
    term = db.IntegerProperty()
    
    payment_mode = db.StringProperty()
    
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    def __unicode__(self):
        return "%s %s %s %s" % (self.created, self.state, self.gender, self.dob)
        
    @permalink
    def get_absolute_url(self):
        return ('efs.views.quote_request_detail', (), {'key': self.key()})
