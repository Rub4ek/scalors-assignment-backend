# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from reminder.models import Reminder


class ReminderAdmin(admin.ModelAdmin):
    model = Reminder
    fields = (
        'email',
        'text',
        'delay',
        'created',
    )
    readonly_fields = (
        'created',
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('delay',)
        return self.readonly_fields


admin.site.register(Reminder, ReminderAdmin)
