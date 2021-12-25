from django.db import models

from accounts.views import register

# Create your models here.


class Accounts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password_1 = models.CharField(max_length=50)
    reg_date = models.DateField()
