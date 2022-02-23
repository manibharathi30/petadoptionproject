from django.db import models
from sqlalchemy import true

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=24)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1,choices=SEX_CHOICES,blank=True)
    submission_date = models.DateField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('vaccine',blank=True)


class Vaccine(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

