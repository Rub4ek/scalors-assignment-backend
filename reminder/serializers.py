from rest_framework import serializers

from reminder.models import Reminder
from reminder.tasks import send_email_reminder

COUNTDOWN_MULTIPLIER = 60


class ReminderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminder
        fields = ('email', 'text', 'delay', 'created', 'url')


class ReminderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('email', 'text', 'delay', 'created')

    def create(self, validated_data):
        instance = super(ReminderDetailSerializer, self).create(validated_data)
        send_email_reminder.apply_async((instance.id,), countdown=instance.delay * COUNTDOWN_MULTIPLIER)
        return instance
