# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from greatesttodo.mixins import NestedViewSetMixin
from todo.models import Board, Todo
from todo.serializers import BoardListSerializer, BoardDetailSerializer, TodoListSerializer, TodoDetailSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """
    Board view set
    
    Allows to:
    - List all boards
    - Add a new board
    - Change a board's title
    - Remove a board
    """
    queryset = Board.objects.all()
    filter_fields = ('todos__done',)

    def get_serializer_class(self):
        if self.action == 'list':
            return BoardListSerializer
        return BoardDetailSerializer


class TodoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Todo view set
    
    Allows to:
    - List all TODOs on a board
    - List only uncompleted TODOs
    - Add TODOs to a board
    - Change a TODOs title or status
    - Delete a TODO
    """
    queryset = Todo.objects.all()
    parent = BoardViewSet
    parent_lookup_field = 'board'
    filter_fields = ('done',)

    def get_serializer_class(self):
        if self.action == 'list':
            return TodoListSerializer
        return TodoDetailSerializer
