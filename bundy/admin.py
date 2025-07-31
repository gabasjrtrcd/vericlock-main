from django.contrib import admin

# Register your models here.
from .models import Person, TimeInRecord, TimeOutRecord

admin.site.register(Person)
admin.site.register(TimeInRecord)
admin.site.register(TimeOutRecord)