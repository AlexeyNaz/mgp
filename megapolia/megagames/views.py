import datetime
import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

from megagames.forms import LoginForm, PlayerForm
from megagames.models import Activity, Player, Event, Ref


class PlayerInfo:
    def __init__(self, login, first, last, score):
        self.LastName = last
        self.FirstName = first
        self.Score = score
        self.Login = login


class StatEl:
    def __init__(self, p, act_count):
        self.act_count = act_count
        self.player = p


def index(request):
    return render(request, "index.html")


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
            return HttpResponse("<h2>Hello,{0}</h2>".format(activity.code))

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
            return render(request, "addScore.html", {'player_name': player.login, 'pid': player.pid, 'code': user.username})
        else:
            return render(request, "playerNotFound.html")

    else:
        players = Player.objects.filter(pid=pid)
        if players.count() > 0:
            pl = players[0]
            evs = Event.objects.filter(player=pl)
            acts = Activity.objects.all()

            class AccPl:
                def __init__(self, act, score, played):
                    self.act = act
                    self.score = score
                    self.played = played

            actPs = []
            for act in acts:
                es = evs.filter(activity=act)
                if es.count() > 0:
                    actPs.append(AccPl(act, es[0].add, True))
                else:
                    actPs.append(AccPl(act, 0, False))

            return render(request, "scorePayer.html", {'player': pl, 'acts': actPs})
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

        Player.objects.create(pid=pid, login=payername, firstName=first_name, lastName=last_name,
                              sub=Ref.objects.get(id=sub), age=age, score=0, lastEvent=datetime.datetime.now())

        return player(request, pid)
    else:
        player_form = PlayerForm()
        player_form.pid = pid
        return render(request, "playerEnter.html", {"form": player_form})


def addScore(pid, act, toAdd):
    pla = Player.objects.get(pid=pid)
    ev = Event.objects.create(activity=act, player=pla, add=toAdd)
    pla.score = pla.score + toAdd
    pla.lastEvent = ev.createAt
    pla.save()
    ev.save()

    return pla


def addWinScore(request, pid, code):
    act = Activity.objects.get(code=code)
    pla = addScore(pid, act, act.win)
    return render(request, "scorePayer.html", {'user': pla})


def addPlayScore(request, pid, code):
    act = Activity.objects.get(code=code)
    pla = addScore(pid, act, act.play)
    return render(request, "scorePayer.html", {'user': pla})


def stat():
    res = []
    players = Player.objects.order_by('-score', 'lastEvent')

    for pla in players:
        ev_count = Event.objects.filter(player=pla).count()
        reselement = StatEl(pla, ev_count)
        res.append(reselement)
    return res


def stat3(request):
    return render(request, "stat3.html", {'stats': stat()[:3]})


def stat10(request):
    return render(request, "stat10.html", {'stats': stat()[:10]})


def fill_db(request):
    for i in range(1000, 2000):
        if Player.objects.filter(pid=i).count() == 0:
            Player.objects.create(pid=i, login=i, firstName=i, lastName=i, sub=Ref.objects.get(id=1), age=i, score=0,
                                  lastEvent=datetime.datetime.now())

    for pl in Player.objects.all():
        for act in Activity.objects.all():
            if random.choice((True, False)):
                addScore(pl.pid, act, act.win)
            else:
                addScore(pl.pid, act, act.play)
