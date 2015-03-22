from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
# Register your models here.

class PollAdmin(admin.ModelAdmin):
    """docstring for PollAdmin"""
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
