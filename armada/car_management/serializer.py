from rest_framework import serializers
from .models import Car
from rest_framework.renderers import JSONRenderer

class CarSerializer(serializers.Serializer):
    data = Car.objects.all()
    serializer = serializers.data
    data_output = JSONRenderer().render(serializer)
    return data_output
