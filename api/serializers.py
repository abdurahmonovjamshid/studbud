from base.models import Room, Topic
from rest_framework import serializers


class RoomSerializler(serializers.ModelSerializer):
    host = serializers.HiddenField(default=serializers.CurrentUserDefault())
    topic = serializers.CharField()

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['participants']

    def create(self, validated_data):
        topic = validated_data.pop('topic')
        topic_instance, created = Topic.objects.get_or_create(name=topic)
        room_instance = Room.objects.create(**validated_data, topic=topic_instance)
        return room_instance
