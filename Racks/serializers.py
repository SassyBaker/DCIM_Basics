from rest_framework import serializers
from .models import RackModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RackModel
        fields = '__all__'
