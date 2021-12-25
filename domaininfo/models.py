from django.db import models
from accounts.models import Accounts

from accounts.views import register
from datetime import date

# Create your models here.


class Domain(models.Model):
    domain_name = models.CharField(max_length=100)
    reg_date = models.DateField(default=date.today)
    planStartDate = models.DateField(default=date.today)
    planEndDate = planStartDate - models.DateField()
    app_name = models.Choices(max_length=200)
    user_name = models.ForeignKey(Accounts)


class Plan(models.Model):
    plan_type = models.CharField(max_length=50)
    plan_price = models.IntegerField(max_length=50)
    storage = models.CharField(max_length=50)


class Server(models.Model):
    server_loc = models.CharField(max_length=100)
    storage = models.ForeignKey(Plan, on_delete=models.CASCADE,)
    domain_name = models.ForeignKey(Domain, on_delete=models.CASCADE,)
    user_name = models.ForeignKey(Accounts)
