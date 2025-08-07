from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Event, Registration


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError('Email already registered')
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError('Username already taken')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class EventModelSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'organizer')

    def validate(self, attrs):
        date = attrs.get('date')
        if date <= date.today():
            raise ValidationError('Date cannot be in the past')
        return attrs


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = ['event', 'user']
        read_only_fields = ('user', 'event')

    def validate(self, data):
        user = self.context['request'].user
        event_pk = self.context['view'].kwargs.get('event_pk')

        try:
            event = Event.objects.get(pk=event_pk)
        except Event.DoesNotExist:
            raise ValidationError("Event not found.")

        if Registration.objects.filter(event=event, user=user).exists():
            raise ValidationError("User already registered for this event.")

        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['event'] = EventModelSerializer(instance.event).data
        data['user'] = UserModelSerializer(instance.user).data
        return data
