# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from reminder.models import Reminder
from reminder.serializers import ReminderListSerializer, ReminderDetailSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    """
    Reminder view set the user to set reminders. 
    A reminder contains an email address, a reminder text and a delay in minutes when it will be triggered. 
    
    Allows to:    
    - List all reminders
    - Create a new reminder
    - Remove a reminder
    """
    queryset = Reminder.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ReminderListSerializer
        return ReminderDetailSerializer
