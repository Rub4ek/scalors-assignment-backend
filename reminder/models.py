# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Reminder(models.Model):
    email = models.EmailField()
    text = models.CharField(max_length=255)
    delay = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{email} {delay} minute(s) since {created}'.format(
            email=self.email,
            delay=self.delay,
            created=self.created.strftime('%Y-%m-%d %H:%M:%S')
        )
