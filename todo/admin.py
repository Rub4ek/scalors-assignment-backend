# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from todo.models import Todo, Board


class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0
    readonly_fields = (
        'created',
        'updated',
    )


class BoardAdmin(admin.ModelAdmin):
    model = Board
    inlines = (
        TodoInline,
    )


admin.site.register(Board, BoardAdmin)
