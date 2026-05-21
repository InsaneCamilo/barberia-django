from django.test import TestCase
from .models import Service
from .models import Appointment


class ServiceModelTest(TestCase):

    def test_create_service(self):

        service = Service.objects.create(
            name='Fade',
            price=30000,
            estimated_time=40
        )

        self.assertEqual(service.name, 'Fade')


class AppointmentTest(TestCase):

    def test_create_appointment(self):

        service = Service.objects.create(
            name='Barba',
            price=15000,
            estimated_time=20
        )

        appointment = Appointment.objects.create(
            customer_name='Camilo',
            phone='123456',
            service=service,
            appointment_date='2026-05-21',
            appointment_time='14:00'
        )

        self.assertEqual(
            appointment.status,
            'pending'
        )