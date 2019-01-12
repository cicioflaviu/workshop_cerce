from django.contrib import admin
from .models import VoteTopic, Vote


class VoteAdmin(admin.ModelAdmin):
    list_display = ["id", "topic", "owner", "vote_value"]
    list_filter = ["owner", "vote_value"]


# Register your models here.
admin.site.register(Vote, VoteAdmin)
admin.site.register(VoteTopic)

