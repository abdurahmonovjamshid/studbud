from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('message', views.MessageViewSet)

router2 = routers.SimpleRouter()
router2.register('topic', views.TopicViewSet)

urlpatterns = [
    path('room/', views.RoomListCreateView.as_view()),
    path('room/<int:pk>/', views.RoomDetailView.as_view()),
    path('room/<int:pk>/messages', views.RoomMessages.as_view()),
    path('', include(router2.urls)),
    path('', include(router.urls))
]
urlpatterns += [
    path('auth', include('rest_framework.urls')),
]
