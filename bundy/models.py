from django.conf import settings
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reference/%Y/%m/%d/', null=True, blank=True)

    def image_url(self):
        if self.image:
            return self.image.url
        return None

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s"/>' % self.image.url)
        return "No Image"

    def __str__(self):
        return self.name
    

class TimeRecord(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=3, choices=[('IN', 'Clock In'), ('OUT', 'Clock Out')])
    image = models.ImageField(upload_to='time_images/%Y/%m/%d/', null=True, blank=True)

    def image_url(self):
        if self.image:
            return self.image.url
        return None

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s"/>' % self.image.url)
        return "No Image"

    def time_tag(self):
        return self.time.astimezone().strftime('%H:%M:%S')

    def __str__(self):
        return f"{self.person.name} - {self.action} - {self.time.strftime('%Y-%m-%d %H:%M:%S')}"
    
