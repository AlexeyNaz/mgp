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
    score = models.IntegerField(db_index=True,  default=0)
    lastEvent = models.DateTimeField(db_index=True, blank=True, default=datetime.datetime.now())

    def __str__(self):
        return self.login


class Activity(models.Model):
    code = models.CharField(max_length=16)
    desc = models.CharField(max_length=1024)
    comment = models.CharField(max_length=1024)
    win = models.IntegerField()
    play = models.IntegerField()
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.desc


class Event(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    add = models.IntegerField()
    createAt = models.DateTimeField(db_index=True, blank=True)

    def __str__(self):
        return self.player.login + "/" + self.activity.desc
