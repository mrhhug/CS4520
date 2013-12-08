from django.db import models

class Measurements(models.Model):
    pass
    
class Measurement(models.Model):
    value = models.FloatField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField('when taken')
    
class Location(models.Model):
    name = models.CharField(max_length=200)
    altitude = models.IntegerField(default=0)
    
class Groups(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Location)
