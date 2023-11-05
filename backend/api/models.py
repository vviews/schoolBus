from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=5, primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    level = models.CharField(max_length=10)
    bus_number=models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.student_id}'
    
    
class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    price = models.IntegerField()
    paid_amount = models.IntegerField(blank=True, default=0, null=True)
    description = models.TextField(blank=True, null=True)
    month = models.CharField(max_length=50)
    monthly = models.CharField(max_length=4, null=True)
    year = models.CharField(max_length=4)
    