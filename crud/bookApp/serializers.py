from rest_framework import serializers
from .models import BookModels

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModels
        fields = '__all__'
