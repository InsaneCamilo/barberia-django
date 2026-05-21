from django.contrib import admin

from .models import Service
from .models import Appointment


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'price',
        'estimated_time'
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'turn_code',
        'customer_name',
        'service',
        'appointment_date',
        'appointment_time',
        'status'
    )

    list_filter = (
        'status',
        'appointment_date'
    )

    search_fields = (
        'customer_name',
        'turn_code'
    )