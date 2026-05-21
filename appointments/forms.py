from django import forms

from .models import Service
from .models import Appointment


class ServiceForm(forms.ModelForm):

    class Meta:

        model = Service

        fields = '__all__'

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'estimated_time': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'name': 'Nombre del servicio',
            'price': 'Precio',
            'estimated_time': 'Tiempo estimado (minutos)',
        }

class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        exclude = ['turn_code', 'status']

        widgets = {

            'customer_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'service': forms.Select(attrs={
                'class': 'form-select'
            }),

            'appointment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'appointment_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
        }

        labels = {
            'customer_name': 'Nombre del cliente',
            'phone': 'Teléfono',
            'service': 'Servicio',
            'appointment_date': 'Fecha de cita',
            'appointment_time': 'Hora de cita',
        }