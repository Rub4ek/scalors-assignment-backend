# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from greatesttodo.mixins import NestedViewSetMixin
from todo.models import Board, Todo
from todo.serializers import BoardListSerializer, BoardDetailSerializer, TodoListSerializer, TodoDetailSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BoardListSerializer
        return BoardDetailSerializer


class TodoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    parent = BoardViewSet
    parent_lookup_field = 'board'

    def get_serializer_class(self):
        if self.action == 'list':
            return TodoListSerializer
        return TodoDetailSerializer
