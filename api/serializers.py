from base.models import Room, Topic, Message, User
from rest_framework import serializers
# from django.contrib.auth.models import User

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'bio')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class RoomSerializler(serializers.ModelSerializer):
    host = serializers.HiddenField(default=serializers.CurrentUserDefault())
    topic = serializers.CharField()

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['participants']

    def create(self, validated_data):
        topic = validated_data.pop('topic').upper()
        topic_instance, created = Topic.objects.get_or_create(name=topic)
        room_instance = Room.objects.create(**validated_data, topic=topic_instance)
        return room_instance

    def update(self, instance, validated_data):
        topic = validated_data.pop('topic').upper()
        name = validated_data.pop('name')
        description = validated_data.pop('description')
        topic_instance, created = Topic.objects.get_or_create(name=topic)
        instance.topic = topic_instance
        instance.name = name
        instance.description = description
        instance.save()
        return instance


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = '__all__'
