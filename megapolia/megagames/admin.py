from django.contrib import admin

# Register your models here.
from megagames.models import Player, Event, Activity

admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Activity)