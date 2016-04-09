from django.contrib import admin
from .models import Game, Contest


# Register your models here.

class ContestAdmin(admin.ModelAdmin):
    list_display = ['game', 'week', 'lineup_set']
    ordering = ['week']

admin.site.register(Game)
admin.site.register(Contest, ContestAdmin)
