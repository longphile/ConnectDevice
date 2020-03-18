from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=25,default="")
    type = models.CharField(max_length=25,default="")
    currentMode = models.CharField(max_length=25,default="")
    desireMode =  models.CharField(max_length=25,default="")
    parameter = models.CharField(max_length=25,default="")
    value = models.CharField(max_length=25,default="")
    threshold_up = models.CharField(max_length=25,default="")
    threshold_down = models.CharField(max_length=25,default="")
    currentState =  models.CharField(max_length=25,default="")
    desireState =  models.CharField(max_length=25,default="")
    connect = models.CharField(max_length=25,default="")
    def __str__(self): #show the actual city name on the dashboard 
        return self.name

    class Meta: #show the plural of city as cities
        verbose_name_plural = 'cities'