from django.urls import path

from reminders.views import RemindersListView, RemindersCreateView


urlpatterns = [
    path('reminder_list/', RemindersListView.as_view(), name='reminders_list'),
    path('reminder_create/', RemindersCreateView.as_view(), name='reminders_create'),
]
