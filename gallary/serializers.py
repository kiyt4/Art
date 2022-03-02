from pyexpat import model
from attr import field
from rest_framework import serializers
from .models import restframework

class demo_restframe(serializers.ModelSerializer):
    class Meta:
        model=restframework
        fields='__all__'