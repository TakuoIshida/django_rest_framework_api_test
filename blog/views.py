import django_filters
from rest_framework import viewsets, filters
from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer
from rest_framework import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author')
    calicurate = serializers.SerializerMethodField()

    def get_calicurate(self):
        a = 1 + 1
        b = 1 +a
        c = b

        return c
