from rest_framework import serializers
from Api.models import home

class homeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'title', 'specification', 'created_at')
        model = home