from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import CreateUserView, CreateEventView, EventListView, UserEventListView, RegistrationCreateView, \
    RegistrationListView

urlpatterns = [
    path('user-create', CreateUserView.as_view()),
    path('event-create', CreateEventView.as_view()),
    path('event-list', EventListView.as_view()),
    path('user-event-list', UserEventListView.as_view()),
    path('registration/<int:event_pk>', RegistrationCreateView.as_view()),
    path('user-registration', RegistrationListView.as_view()),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
