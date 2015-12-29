from django.contrib import admin
from .models import VideoGame, Challenge, BracketMatch
# Register your models here.


def email(modeladmin, request, queryset):
    for q in queryset:
        q.send_mail()
email.short_description = 'Email'


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['game', 'week', 'lineup_set']
    ordering = ['game']
    actions = [email]

admin.site.register(VideoGame)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(BracketMatch)
