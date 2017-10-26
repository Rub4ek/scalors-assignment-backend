from rest_framework import serializers

from reminder.models import Reminder
from reminder.tasks import send_email_reminder

COUNTDOWN_MULTIPLIER = 60


class ReminderListSerializer(serializers.HyperlinkedModelSerializer):
    """
    List model serializer for Reminder model
    """
    class Meta:
        model = Reminder
        fields = ('email', 'text', 'delay', 'created', 'url')


class ReminderDetailSerializer(serializers.ModelSerializer):
    """
    Detail model serializer for Reminder model
    Sends an email on create
    """
    class Meta:
        model = Reminder
        fields = ('email', 'text', 'delay', 'created')

    def create(self, validated_data):
        """
        Create a Reminder instance and send delayed celery task to send email
        :param validated_data: 
        :return: 
        """
        instance = super(ReminderDetailSerializer, self).create(validated_data)
        send_email_reminder.apply_async((instance.id,), countdown=instance.delay * COUNTDOWN_MULTIPLIER)
        return instance
