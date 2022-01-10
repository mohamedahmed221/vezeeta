from datetime import time
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Appointments(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='client')
    consultant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='consultant')
    available_timings = models.ForeignKey(
        "AvailableTimings", on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    consulting_fee = models.CharField(max_length=50,  blank=True, null=True)
    booking_Fee = models.CharField(max_length=50,  blank=True, null=True)
    total = models.CharField(max_length=50,  blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    appointment_date_start = models.DateTimeField(blank=True, null=True)
    appointment_date_end = models.DateTimeField(blank=True, null=True)
    PENDING = 'PENDING'
    Underway = 'Underway'
    COMPLETE = 'COMPLETE'
    Refunded = 'Refunded'
    Status_select = [
        (PENDING, 'PENDING'),
        (Underway, 'Underway'),
        (COMPLETE, 'COMPLETE'),
        (Refunded, 'Refunded'),
    ]
    status = models.CharField(
        max_length=13,
        choices=Status_select,
        default=PENDING,
    )
    client_first_name = models.CharField(
        max_length=100,  blank=True, null=True)
    client_last_name = models.CharField(max_length=100,  blank=True, null=True)
    client_phone = models.CharField(max_length=100,  blank=True, null=True)
    client_email = models.CharField(max_length=100,  blank=True, null=True)

    def __str__(self):
        return f"{self.consultant} - {self.client}"


class AvailableDate(models.Model):
    consultant = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.day}"


class AvailableTimings(models.Model):
    day = models.ForeignKey(
        AvailableDate, on_delete=models.CASCADE, )
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.day}- {self.time_start} - {self.time_end}"
