from rest_framework import serializers

from reminder.models import Reminder


class ReminderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminder
        fields = ('email', 'text', 'delay', 'created', 'url')


class ReminderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('email', 'text', 'delay', 'created')
