# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from todo import models


class TodoInline(admin.TabularInline):
    model = models.Todo
    extra = 0
    readonly_fields = (
        'created',
        'updated',
    )


class BoardAdmin(admin.ModelAdmin):
    model = models.Board
    inlines = (
        TodoInline,
    )


admin.site.register(models.Board, BoardAdmin)
