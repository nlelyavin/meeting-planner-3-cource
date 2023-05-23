from django.contrib import admin

from meeting_planner.models import Team, CustomUser, TeamToUser


class TeamToUserInline(admin.TabularInline):
    model = TeamToUser
    extra = 3


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'team_creator', ]
    inlines = [TeamToUserInline]


@admin.register(CustomUser)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['username']
    # inlines = [TeamUserInline]
