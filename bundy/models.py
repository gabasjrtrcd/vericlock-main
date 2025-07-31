from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class TimeInRecord(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='time_in_images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f"{self.person.name} - IN {self.time_in.strftime('%Y-%m-%d %H:%M:%S')}"
    

class TimeOutRecord(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time_out = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='time_out_images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f"{self.person.name} - OUT {self.time_out.strftime('%Y-%m-%d %H:%M:%S')}"
    
