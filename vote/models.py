
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model, TextField, ForeignKey, DateTimeField, IntegerField


class VoteTopic(Model):
    proposal = TextField(help_text="The proposal text")
    owner = ForeignKey(User, on_delete=models.CASCADE)

    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Proposal by {}: {}".format(self.owner, self.proposal)

    def vote_results(self):
        results = {}
        for i in Vote.VOTE_OPTIONS:
            results[i[1]] = self.vote_set.filter(vote_value=i[0]).count()
        return results


class Vote(Model):
    VOTE_NO = 0
    VOTE_YES = 1
    VOTE_ABS = 2

    VOTE_OPTIONS = (
        (VOTE_YES, "yes"),
        (VOTE_NO, "no"),
        (VOTE_ABS, "abstain")
    )

    owner = ForeignKey(User, on_delete=models.CASCADE)
    created = DateTimeField(auto_now_add=True)
    vote_value = IntegerField(choices=VOTE_OPTIONS)

    topic = ForeignKey(VoteTopic, on_delete=models.CASCADE)

    def __str__(self):
        return "{} vote {} for #{}".format(self.owner, self.get_vote_value_display(), self.topic.id)
