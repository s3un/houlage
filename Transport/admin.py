from django.contrib import admin
from .models import Vehicle,Booking,Brand, AutoMobile,Rent,Locations
# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Brand)
admin.site.register(AutoMobile)
admin.site.register(Rent)
admin.site.register(Locations)