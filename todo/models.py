# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    board = models.ForeignKey('Board', related_name='todos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Board(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
