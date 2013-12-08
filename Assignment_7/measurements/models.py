from django.db import models

class Measurement(models.Model):
    value = models.FloatField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField('when taken')
    
class Location(models.Model):
    name = models.CharField(max_length=200)
    altitude = models.IntegerField('Altitude in feet')
    
    def __unicode__(self):
        return self.name
        
class Group(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Location)
    
    def __unicode__(self):
        return self.name
    
# measurements
