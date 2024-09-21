from django.shortcuts import render

from rest_framework import viewsets
from .models import Doctor,Specialization,Designation,AvailbeTime,Review
from .import serializers
# Create your views here.

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class AvailbeTimeViewset(viewsets.ModelViewSet):
    queryset = AvailbeTime.objects.all()
    serializer_class = serializers.AvailbeTimeSerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer