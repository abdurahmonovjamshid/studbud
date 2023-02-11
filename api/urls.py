from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('message', views.MessageViewSet)

urlpatterns = [
    path('room/', views.RoomListCreateView.as_view()),
    path('room/<int:pk>/', views.RoomDetailView.as_view()),
    path('topic/', views.TopicListView.as_view()),
    path('', include(router.urls))

]
