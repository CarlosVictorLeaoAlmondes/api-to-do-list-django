from rest_framework import serializers
from toDo import models

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ToDo
        fields = '__all__'