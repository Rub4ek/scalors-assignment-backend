# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from reminder.models import Reminder


class ReminderTests(APITestCase):

    def test_create_reminder(self):
        url = reverse('reminder-list')
        response = self.client.post(url, {'email': 'test@example.com', 'delay': 1, 'text': 'Test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 1)
        self.assertEqual(Reminder.objects.get().email, 'test@example.com')

    def test_update_reminder(self):
        reminder = Reminder.objects.create(email='test@example.com', delay=1)
        url = reverse('reminder-detail', kwargs={'pk': reminder.pk})
        response = self.client.patch(url, {'email': 'updated@example.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Reminder.objects.count(), 1)
        self.assertEqual(Reminder.objects.get().email, 'updated@example.com')

    def test_delete_reminder(self):
        reminder = Reminder.objects.create(email='test@example.com', delay=1)
        url = reverse('reminder-detail', kwargs={'pk': reminder.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_reminder(self):
        Reminder.objects.create(email='test@example.com', delay=1)
        url = reverse('reminder-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_reminder(self):
        reminder = Reminder.objects.create(email='test@example.com', delay=1)
        url = reverse('reminder-detail', kwargs={'pk': reminder.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Reminder.objects.get().email, 'test@example.com')
