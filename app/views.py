from django.shortcuts import render
from .models import ContactSerializer, Contact
from rest_framework import generics


class ContactViewSet(generics.CreateAPIView):
    serializer_class = ContactSerializer