from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework_nested import routers

from todo.views import BoardViewSet, TodoViewSet

# TODO: Found a way to make work several routers with drf html renderer
router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet, base_name='board')
board_router = routers.NestedDefaultRouter(router, r'boards', lookup='board')
board_router.register(r'todos', TodoViewSet, base_name='todo')

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/api/')),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(board_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
