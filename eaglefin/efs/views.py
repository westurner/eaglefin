# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from ragendja.template import render_to_response

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, \
    update_object

from efs.models import *
from efs.forms import QuoteRequestForm

def quote_request_create(request):
    return create_object(request, form_class=QuoteRequestForm,
        post_save_redirect=reverse('efs.views.quote_request_detail',
                                   kwargs=dict(key='%(key)s')))

def quote_request_detail(request, key):
    return object_detail(request, QuoteRequest.all(), key)
