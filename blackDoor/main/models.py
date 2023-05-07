from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from django.db import models


class User(AbstractUser, PermissionsMixin):
    username = None
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    work_experience = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=32)

    class Meta:
        db_table = 'Employee'


class Sketch(models.Model):
    sketch_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=128)
    price = models.FloatField()

    class Meta:
        db_table = 'Sketch'


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=128, null=True, blank=True)
    status = models.CharField(max_length=32)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sketch = models.ForeignKey(Sketch, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Session'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    body = models.CharField(max_length=1024)

    class Meta:
        db_table = 'Review'
