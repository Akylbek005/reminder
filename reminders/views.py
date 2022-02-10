from rest_framework import generics

from reminders.models import Reminders
from reminders.serializers import RemindersSerializer


class RemindersListView(generics.ListAPIView):
    queryset = Reminders.objects.all()
    serializer_class = RemindersSerializer


class RemindersCreateView(generics.CreateAPIView):
    queryset = Reminders.objects.all()
    serializer_class = RemindersSerializer
