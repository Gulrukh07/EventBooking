from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, DateField, ForeignKey, CASCADE




class Event(Model):
    title = CharField(max_length=255)
    description = TextField()
    location = CharField(max_length=255)
    date = DateField()
    organizer = ForeignKey(User, on_delete=CASCADE, related_name='events')

class Registration(Model):
    event = ForeignKey('apps.Event', on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    registration_date = DateField(auto_now_add=True)