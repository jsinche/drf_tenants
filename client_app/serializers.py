from rest_framework import serializers
from django_tenants.models import TenantMixin
from app.models import Client  # o el modelo específico de cliente para los tenants

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'