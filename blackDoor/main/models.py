from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.db import models


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=32, unique=True)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    date_of_birth = models.DateField(null=False, blank=False)
    tattoos_made = models.PositiveIntegerField(default=0, blank=True)
    photo = models.ImageField(upload_to='user_photos', default='user_photos/default_image.png', blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"




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
    photo = models.ImageField(upload_to='sketch_photos', default='default_image.png')  # Поле с фотографией
    price = models.FloatField()

    class Meta:
        db_table = 'Sketch'


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=32, default='In progress')
    employee_id = models.IntegerField(null=False, blank=False)
    sketch = models.ForeignKey(Sketch, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Session'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(null=False, blank=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    body = models.CharField(max_length=1024)
    rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        db_table = 'Review'
