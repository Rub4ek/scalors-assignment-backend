from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

import models


class TodoListSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'board_pk': 'board__pk',
    }

    class Meta:
        model = models.Todo
        fields = ('title', 'done', 'url',)


class TodoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Todo
        fields = ('title', 'done', 'created', 'updated',)


class BoardListSerializer(serializers.HyperlinkedModelSerializer):
    todo_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Board
        fields = ('name', 'todo_count', 'url',)

    @staticmethod
    def get_todo_count(obj):
        return obj.todos.count()


class BoardDetailSerializer(serializers.ModelSerializer):
    todos = TodoListSerializer(many=True, read_only=True)
    todos_url = serializers.HyperlinkedIdentityField(view_name='todo-list', lookup_url_kwarg='board_pk')

    class Meta:
        model = models.Board
        fields = ('name', 'todos', 'todos_url',)
