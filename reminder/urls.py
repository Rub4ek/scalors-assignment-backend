from django.conf.urls import url, include
from rest_framework_nested import routers

from reminder.views import ReminderViewSet

root_router = routers.DefaultRouter()
root_router.register(r'reminders', ReminderViewSet, base_name='reminder')


urlpatterns = [
    url(r'^', include(root_router.urls)),
]
