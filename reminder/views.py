# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from reminder.models import Reminder
from reminder.serializers import ReminderListSerializer, ReminderDetailSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ReminderListSerializer
        return ReminderDetailSerializer
