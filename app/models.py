from django.db import models

# Create your models here.

class Employee(models.Model):
    EName=models.CharField(max_length=100)
    ESal=models.IntegerField()
    EJob=models.CharField(max_length=100)

    def __str__(self):
        return self.EName
    