from django.contrib import admin
from .models import Appointments, AvailableDate, AvailableTimings
# Register your models here.


admin.site.register(Appointments)
admin.site.register(AvailableDate)
admin.site.register(AvailableTimings)
