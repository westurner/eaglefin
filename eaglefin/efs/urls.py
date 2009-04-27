# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('efs.views',
    (r'^quote/new$', 'quote_request_create'),
    (r'^quote/(?P<key>.+)$', 'quote_request_detail'),

)
