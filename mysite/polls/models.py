from django.db import models
from django.utils import timezone
# Create your models here.
class Poll(models.Model):
    """docstring for Poll"""
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question
class Choice(models.Model):
    """docstring for Choice"""
    poll = models.ForeignKey(Poll)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_test


