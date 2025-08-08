from django.contrib import admin

# Register your models here.
from .models import Person, TimeRecord


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'image_tag', 'location']
    list_display = ['name', 'image_tag', 'location']


@admin.register(TimeRecord)
class TimeRecordAdmin(admin.ModelAdmin):
    fields = ['person', 'action', 'time', 'image_tag']
    list_display = ['person', 'action', 'time', 'image_tag']
    readonly_fields = ['person', 'action', 'time', 'image_tag']

