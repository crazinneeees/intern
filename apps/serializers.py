
from rest_framework.serializers import ModelSerializer, CharField, DateTimeField

from apps.models import CustomUser, Event, Registration

from django.contrib.auth.hashers import make_password

class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def validate_password(self, value):
        return make_password(value)




class CreateEventSerializer(ModelSerializer):
    date = DateTimeField()
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'location', 'organizer')



class CreateRegisterEventSerializer(ModelSerializer):
    registered_at = DateTimeField(format="%d/%m/%Y %H:%M")
    class Meta:
        model = Registration
        fields = ('user', 'event', 'registered_at')


class ListEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'location', 'organizer')


class ListRegisterEventSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = ('event', 'registered_at')