from _ctypes import Array
from typing import List

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from megagames.forms import LoginForm, PlayerForm
from megagames.models import Activity, Player, Event


def loginU(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        activities = Activity.objects.filter(code=name, password=password)

        if activities.count() > 0:
            activity = activities.first()

            users = User.objects.filter(username=name, password=password)
            if users.count() > 0:
                user = users.first()
            else:
                user = User.objects.create(username=name, password=password)

            authenticate(username=user.username, password=user.password)
            login(request, user)
            return HttpResponse("<h2>Hello, {0}</h2>".format(activity.code))

    user_form = LoginForm()
    return render(request, "login.html", {"form": user_form})


def logoutU(request):
    logout(request)
    return loginU(request)


def player(request, pid):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        players = Player.objects.filter(pid=pid)
        if players.count() > 0:
            player = players.first()
            return render(request, "addScore.html",
                          {'player_name': player.login, 'pid': player.pid, 'code': user.username})
        else:
            return render(request, "playerNotFound.html")

    else:
        players = Player.objects.filter(pid=pid)
        if players.count() > 0:
            events = Event.objects.filter(player__pid=pid)

            add = events.aggregate(Sum('add')).get('add__sum', 0.00)

            if add is None:
                add = 0

            userinfo = players[0].login

            return render(request, "scorePayer.html", {'total': add, 'user': userinfo})
        else:
            return playerEnter(request, pid)


def playerEnter(request, pid):
    if request.method == "POST":
        payername = request.POST.get("login")
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        sub = request.POST.get("sub")
        age = request.POST.get("age")
        pid = request.POST.get("pid")

        Player.objects.create(pid=pid, login=payername, firstName=first_name, lastName=last_name, sub=sub, age=age)

        return player(request, pid)
    else:
        player_form = PlayerForm()
        player_form.pid = pid
        return render(request, "playerEnter.html", {"form": player_form})


def addWinScore(request, pid, code):
    pla = Player.objects.get(pid=pid)
    act = Activity.objects.get(code=code)

    ev = Event.objects.create(activity=act, player=pla, add=act.win, subs=0)
    ev.save()

    events = Event.objects.filter(player__pid=pid)
    add = events.aggregate(Sum('add')).get('add__sum', 0.00)
    if add is None:
        add = 0
    userinfo = pla.login
    return render(request, "scorePayer.html", {'total': add, 'user': userinfo})


def addPlayScore(request, pid, code):
    pla = Player.objects.get(pid=pid)
    act = Activity.objects.get(code=code)

    ev = Event.objects.create(activity=act, player=pla, add=act.play, subs=0)
    ev.save()

    events = Event.objects.filter(player__pid=pid)
    add = events.aggregate(Sum('add')).get('add__sum', 0.00)
    if add is None:
        add = 0
    userinfo = pla.login
    return render(request, "scorePayer.html", {'total': add, 'user': userinfo})


def stat(request, count):
    res = []
    players = Player.objects.all()

    class StatEl:
        def __init__(self, a, p):
            self.add = a
            self.player = p

    for player in players:
        add = Event.objects.filter(player__pid=player.pid).aggregate(Sum('add')).get('add__sum', 0.00)
        if add is None:
            add = 0

        reselement = StatEl(add, player)
        res.append(reselement)

    def myFunc(e):
        return e.add

    res.sort(reverse=True,key=myFunc)
    len = int(count)
    return render(request, "stat.html", {'stats': res[:len]})


