from django.contrib.auth.models import User
from rest_framework import viewsets
from lovely_parking_project.lovely_parking_app import serializers
from lovely_parking_project.lovely_parking_app.models import Location

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
	
class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = serializers.LocationSerializer