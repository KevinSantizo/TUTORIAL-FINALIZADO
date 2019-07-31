from django.db import models
from django import forms

# Create your models here.


class Crane(models.Model):
    license_plate = models.CharField(max_length=50, help_text="Enter a License Plate for you Crane")
    trademark = models.CharField(max_length=50, help_text='Enter Trademark of you Crane')
    year = models.IntegerField()
    characteristic = models.CharField(max_length=100, help_text='Describe Crane characteristic')

    def __str__(self):
        return self.trademark + ' -- ' + self.characteristic


class Pilot(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter your name')
    last_name = models.CharField(max_length=100, help_text='Enter your last name')
    DPI = models.CharField(max_length=13, help_text='Enter your DPI')

    def __str__(self):
        return self.first_name + ' --- ' + self.last_name


class Assignment(models.Model):
    LOAN_STATUS = (
        ('o', 'On Route'),
        ('a', 'Available'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='o',
        help_text='Crane availability',
    )
    start_time = models.DateTimeField()
    pilot_assigned = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    crane_assigned = models.ForeignKey(Crane, on_delete=models.CASCADE)

    def __str__(self):
        return self.status + ' Pilot: ' + self.pilot_assigned.first_name + ' Crane: ' + self.crane_assigned.license_plate



