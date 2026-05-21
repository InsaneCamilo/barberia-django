from django.db import models
import uuid


class Service(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    estimated_time = models.IntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('attending', 'En atención'),
        ('completed', 'Finalizado'),
        ('cancelled', 'Cancelado'),
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    turn_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.turn_code:

            while True:

                code = f'B{uuid.uuid4().hex[:5].upper()}'

                if not Appointment.objects.filter(turn_code=code).exists():
                    self.turn_code = code
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name