from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField
from .models import Room
from users.serializers import TinyUserSerializer


class RoomSerializer(serializers.ModelSerializer):
    
    user = TinyUserSerializer()
    
    class Meta:
        model = Room
        fields = ("pk", 'name', 'price', 'instant_book', 'user')


class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()