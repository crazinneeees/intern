from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.models import CustomUser, Event, Registration
from apps.serializers import RegisterSerializer, CreateEventSerializer, CreateRegisterEventSerializer, \
    ListEventSerializer, ListRegisterEventSerializer


# Create your views here.


class RegisterCustomUserView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class CreateEventView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = CreateEventSerializer


class RegisterEventView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateRegisterEventSerializer


class ListEventView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListEventSerializer

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class ListRegistrationsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListRegisterEventSerializer

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
