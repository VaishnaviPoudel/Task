from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now=True)


class WaterIntakeGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_goal_amount = models.IntegerField(default=2000)