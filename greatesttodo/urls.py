from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework_nested import routers

from reminder.views import ReminderViewSet
from todo.views import BoardViewSet, TodoViewSet

# TODO: Found a way to make work several routers with drf html renderer
root_router = routers.DefaultRouter()

# To do routes
root_router.register(r'boards', BoardViewSet, base_name='board')
board_router = routers.NestedDefaultRouter(root_router, r'boards', lookup='board')
board_router.register(r'todos', TodoViewSet, base_name='todo')

# Reminder routes
root_router.register(r'reminders', ReminderViewSet, base_name='reminder')

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/api/')),
    url(r'^api/', include(root_router.urls)),
    url(r'^api/', include(board_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
