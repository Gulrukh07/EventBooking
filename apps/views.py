from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Event, Registration
from apps.serializers import UserModelSerializer, EventModelSerializer, RegistrationSerializer


# Create your views here.

@extend_schema(tags=['user'])
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['event'])
class CreateEventView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


@extend_schema(tags=['user'])
class UserEventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(organizer=self.request.user)


@extend_schema(tags=['event'])
class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer


@extend_schema(tags=['registration'])
class RegistrationCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        event_pk = self.kwargs['event_pk']
        event = Event.objects.get(pk=event_pk)
        if event:
            serializer.save(user=self.request.user, event=event)


@extend_schema(tags=['registration'])
class RegistrationListView(ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(user=self.request.user)
