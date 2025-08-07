from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import RegisterCustomUserView, CreateEventView, RegisterEventView, ListEventView, \
    ListRegistrationsListView

urlpatterns = [
    path('register', RegisterCustomUserView.as_view()),
    path('create-event', CreateEventView.as_view()),
    path('register-event', RegisterEventView.as_view()),
    path('events-list', ListEventView.as_view()),
    path('registration-list', ListRegistrationsListView.as_view()),
]