from django.urls import path, include
from django.contrib.auth.models import Link
from rest_framework import routers,  serializers

# Serializers define the API representation.


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
