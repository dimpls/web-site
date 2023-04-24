from django.db import models

# Create your models here.


class Master(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    work_experience = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=32)

    class Meta:
        db_table = 'Employee'

