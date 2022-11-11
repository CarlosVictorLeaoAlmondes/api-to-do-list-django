from rest_framework import viewsets
from toDo.api import serializers
from toDo import models


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ToDoSerializer
    queryset = models.ToDo.objects.all()
