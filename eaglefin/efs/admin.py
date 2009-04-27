from django.contrib import admin
from efs.models import QuoteRequest
from efs.forms import QuoteRequestForm

class QuoteRequestAdmin(admin.ModelAdmin):
    form = QuoteRequestForm

    list_display = ('created','coverage','term','state','gender','height','weight',)

admin.site.register(QuoteRequest, QuoteRequestAdmin)
