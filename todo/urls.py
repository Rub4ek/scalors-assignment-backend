from django.conf.urls import url, include
from rest_framework_nested import routers

from todo.views import BoardViewSet, TodoViewSet

root_router = routers.DefaultRouter()
root_router.register(r'boards', BoardViewSet, base_name='board')
board_router = routers.NestedDefaultRouter(root_router, r'boards', lookup='board')
board_router.register(r'todos', TodoViewSet, base_name='todo')


urlpatterns = [
    url(r'^', include(root_router.urls)),
    url(r'^', include(board_router.urls)),
]
