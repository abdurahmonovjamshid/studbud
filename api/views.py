from rest_framework import generics, viewsets
from base.models import Room, Topic, Message
from .serializers import RoomSerializler, TopicSerializer, MessageSerializer
from rest_framework import permissions
from .permissions import RoomOwnerOrReadonly, MessageOwnerOrReadonly


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializler


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializler
    permission_classes = (RoomOwnerOrReadonly,)


class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (MessageOwnerOrReadonly, permissions.IsAuthenticatedOrReadOnly)
