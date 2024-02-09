from rest_framework import serializers
from .models import Car
from rest_framework.renderers import JSONRenderer

class CarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Car
        fields = [
            'legal_number',
            'image_vehicle_number',
            'police_number',
            'release_year',
            'color',
            'series',
            'total_distance',
            'price',
            'car_type',
            'car_image',
            'created_at',
            'updated_at',
            'brand_id',
            'category_id',
            'transmission_id',
        ]
