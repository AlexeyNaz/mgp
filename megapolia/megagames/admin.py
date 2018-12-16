import datetime

from django.contrib import admin

# Register your models here.
from megagames.models import Player, Event, Activity


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('pid', 'login', 'firstName', 'lastName', 'sub', 'age', 'score', 'lastEvent')


def delete_event_full(modeladmin, request, queryset):
    for e in queryset:
        pla = Player.objects.get(pid=e.player.pid)
        pla.score = pla.score - e.add

        e.delete()
        lastev = Event.objects.filter(player_id=pla.id).order_by('-createAt')

        if lastev.count() > 0:
            pla.lastEvent = lastev.first().createAt
        else:
            pla.lastEvent = datetime.datetime.min()

        print(str(pla.lastEvent) + '/' + str(pla.score))
        #raise Error(pla.lastEvent + '/' + pla.score)

        pla.save()


class EventAdmin(admin.ModelAdmin):
    list_display = ('activity', 'player', 'add', 'createAt')
    list_filter = ('activity', 'player', 'createAt')

    actions = [delete_event_full]



class ActivityAdmin(admin.ModelAdmin):
    list_display = ('code', 'desc', 'win', 'play', 'password')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Activity, ActivityAdmin)