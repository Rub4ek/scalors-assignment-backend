from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from greatesttodo.routers import ExtendableRouter
from todo.urls import root_router as todo_root_router
from todo.urls import board_router as todo_nested_router
from reminder.urls import root_router as reminder_root_router

api_root_router = ExtendableRouter()
api_root_router.extend(todo_root_router)
api_root_router.extend(reminder_root_router)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/api/')),
    url(r'^api/', include(api_root_router.urls)),
    url(r'^api/', include(todo_nested_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
