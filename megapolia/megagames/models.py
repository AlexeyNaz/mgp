import datetime

from django.db import models


# Create your models here.
class Ref(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16)


class Player(models.Model):
    pid = models.CharField(max_length=4)
    login = models.CharField(max_length=32)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    sub = models.ForeignKey(Ref, null=True, on_delete=models.SET_NULL)
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
    createAt = models.DateTimeField(blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.createAt = datetime.datetime.now()