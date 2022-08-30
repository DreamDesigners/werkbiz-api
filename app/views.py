from django.shortcuts import render
from .models import ContactSerializer, Contact
from rest_framework import viewsets


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer