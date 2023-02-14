from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Room, Topic, Message
from .serializers import RoomSerializler, TopicSerializer, MessageSerializer
from rest_framework import permissions
from .permissions import RoomOwnerOrReadonly, MessageOwnerOrReadonly, IsAdminOrReadOnly


class RoomMessages(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            room = None
        if not room:
            return Response('not found', status=400)
        serializer = MessageSerializer(room.message_set.all(), many=True)

        return Response(serializer.data)


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializler


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializler
    permission_classes = (RoomOwnerOrReadonly,)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly,)

    @action(methods=['get'], detail=True)
    def rooms(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            topic = None
        if not topic:
            return Response('not found', status=400)
        serializer = TopicSerializer(topic.room_set.all(), many=True)
        return Response(serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (MessageOwnerOrReadonly, permissions.IsAuthenticatedOrReadOnly)
