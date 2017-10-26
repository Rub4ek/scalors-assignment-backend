# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from todo.models import Board, Todo


class BoardsTests(APITestCase):

    def test_create_board(self):
        url = reverse('board-list')
        response = self.client.post(url, {'name': 'Test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Board.objects.count(), 1)
        self.assertEqual(Board.objects.get().name, 'Test')

    def test_update_board(self):
        board = Board.objects.create(name='Test')
        url = reverse('board-detail', kwargs={'pk': board.pk})
        response = self.client.patch(url, {'name': 'Updated'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Board.objects.count(), 1)
        self.assertEqual(Board.objects.get().name, 'Updated')

    def test_delete_board(self):
        board = Board.objects.create(name='Test')
        url = reverse('board-detail', kwargs={'pk': board.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_board(self):
        Board.objects.create(name='Test')
        url = reverse('board-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_board(self):
        board = Board.objects.create(name='Test')
        url = reverse('board-detail', kwargs={'pk': board.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Board.objects.get().name, 'Test')


class TodosTests(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(TodosTests, cls).setUpClass()
        cls.board = Board.objects.create(name='Test')

    def test_create_todo(self):
        url = reverse('todo-list', kwargs={'board_pk': self.board.pk})
        response = self.client.post(url, {'title': 'Test', 'done': True}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test')

    def test_update_todo(self):
        todo = Todo.objects.create(title='Test', board_id=self.board.id)
        url = reverse('todo-detail', kwargs={'board_pk': self.board.pk, 'pk': todo.pk})
        response = self.client.patch(url, {'title': 'Updated'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Updated')

    def test_delete_todo(self):
        todo = Todo.objects.create(title='Test', board_id=self.board.id)
        url = reverse('todo-detail', kwargs={'board_pk': self.board.pk, 'pk': todo.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_todo(self):
        Todo.objects.create(title='Test', board_id=self.board.id)
        url = reverse('todo-list', kwargs={'board_pk': self.board.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_todo(self):
        todo = Todo.objects.create(title='Test', board_id=self.board.id)
        url = reverse('todo-detail', kwargs={'board_pk': self.board.pk, 'pk': todo.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.get().title, 'Test')
