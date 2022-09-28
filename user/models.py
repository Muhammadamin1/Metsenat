from django.contrib.auth.models import AbstractUser
from django.db import models

from metsenat.models import BaseModel


class University(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Student(BaseModel):
    class Degree(models.TextChoices):
        BACHELOR = 'Bakalavr'
        MASTER = 'Magister'

    full_name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students', null=True)
    degree = models.CharField(max_length=10, choices=Degree.choices, default=Degree.BACHELOR)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    contract_amount = models.BigIntegerField(null=True)

    def __str__(self):
        return self.full_name


class Sponsor(BaseModel):
    class Type(models.TextChoices):
        PHYSICAL_PERSON = 'Jismoniy shaxs'
        LEGAL_PERSON = 'Yuridik shaxs'

    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    type = models.CharField(max_length=15, choices=Type.choices, default=Type.PHYSICAL_PERSON)
    payment_amount = models.BigIntegerField(null=True)
    organization = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.full_name

