from django.db import models


# Create your models here.
class Player(models.Model):
    pid = models.CharField(max_length=4)
    login = models.CharField(max_length=32)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    sub = models.CharField(max_length=32)
    age = models.IntegerField()


class Activity(models.Model):
    code = models.CharField(max_length=16)
    desc = models.CharField(max_length=1024)
    comment = models.CharField(max_length=1024)
    win = models.IntegerField()
    play = models.IntegerField()
    password = models.CharField(max_length=16)


class Event(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    add = models.IntegerField()

