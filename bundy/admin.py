from django.contrib import admin

# Register your models here.
from .models import Person, TimeRecord


class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'location']
    list_display = ['name', 'image', 'location']


class TimeRecordAdmin(admin.ModelAdmin):
    fields = ['person', 'action', 'time', 'image_tag']
    list_display = ['person', 'action', 'time', 'image_tag']
    readonly_fields = ['person', 'action', 'time', 'image_tag']


admin.site.register(Person, PersonAdmin)
admin.site.register(TimeRecord, TimeRecordAdmin)
