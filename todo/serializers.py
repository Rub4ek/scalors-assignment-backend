from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from todo.models import Todo, Board


class TodoListSerializer(NestedHyperlinkedModelSerializer):
    """
    List hyperlinked model serializer for Todo model
    """
    parent_lookup_kwargs = {
        'board_pk': 'board__pk',
    }

    class Meta:
        model = Todo
        fields = ('title', 'done', 'url',)


class TodoDetailSerializer(serializers.ModelSerializer):
    """
    Detail model serializer for Reminder model
    """

    class Meta:
        model = Todo
        fields = ('title', 'done', 'created', 'updated',)


class BoardListSerializer(serializers.HyperlinkedModelSerializer):
    """
    List hyperlinked model serializer for Board model
    """
    todo_count = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('name', 'todo_count', 'url',)

    @staticmethod
    def get_todo_count(obj):
        return obj.todos.count()


class BoardDetailSerializer(serializers.ModelSerializer):
    """
    Detail model serializer for Board model
    """
    todos = TodoListSerializer(many=True, read_only=True)
    todos_url = serializers.HyperlinkedIdentityField(view_name='todo-list', lookup_url_kwarg='board_pk')

    class Meta:
        model = Board
        fields = ('name', 'todos', 'todos_url',)
