from django.db import models
from rest_framework import serializers


class Contact(models.Model):
    full_name         = models.CharField(max_length=400, null=True, blank=True)
    email             = models.EmailField(null=True, blank=True)
    phone             = models.CharField(max_length=12, null=True, blank=True)
    company           = models.CharField(max_length=255, null=True, blank=True)
    description       = models.TextField(null=True, blank=True)

    is_reviewd        = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name + str(self.email) + self.phone


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'