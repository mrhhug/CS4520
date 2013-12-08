from django.contrib import admin
from measurements.models import Group, Location, Measurement

class LcoationChoiceInline(admin.StackedInline):
    model = Location#Measurement
    extra = 1

class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','altitude']}),
    ]
    inlines = [LcoationChoiceInline]

class GroupAdmin(admin.ModelAdmin):
    filter_vertical = ("members",)
        
admin.site.register(Group,GroupAdmin)
admin.site.register(Location,LocationAdmin)
# measurements
