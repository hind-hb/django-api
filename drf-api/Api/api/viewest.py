
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from Api.api.serializer import homeSerializer
from Api.models import home


class homeList(generics.ListCreateAPIView):
    queryset = home.objects.all()
    serializer_class = homeSerializer

class homeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = home.objects.all()
    serializer_class = homeSerializer
