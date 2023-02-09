from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomListCreateView.as_view()),
    path('<int:pk>/', views.RoomDetailView.as_view())
]
