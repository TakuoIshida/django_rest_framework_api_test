from rest_framework import serializers
from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Entry
        fields = '__all__'


        