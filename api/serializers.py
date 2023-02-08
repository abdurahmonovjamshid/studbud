from base.models import Room
from rest_framework import serializers


class RoomSerializler(serializers.ModelSerializer):
    host = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['participants']
