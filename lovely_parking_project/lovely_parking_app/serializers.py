from django.contrib.auth.models import User
from rest_framework import serializers

from lovely_parking_project.lovely_parking_app.models import Location

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
		
class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('name', 'address', 'coordinates')