from django.contrib import admin

from .models import Vehicle, Driver, Route, VehicleStatus

admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(VehicleStatus)
