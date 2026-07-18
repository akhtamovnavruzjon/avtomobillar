from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .models import Cars
from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CarList(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


class CarUpdate(UpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

class CarCreate(CreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

class CarDelete(DestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


class CarDetail(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

