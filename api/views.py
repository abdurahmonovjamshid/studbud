from rest_framework import generics
from base.models import Room
from .serializers import RoomSerializler


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializler
