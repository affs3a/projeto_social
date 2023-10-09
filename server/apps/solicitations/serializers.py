from rest_framework import serializers
from .models import User


class SolicitationSerialize(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        read_only_fields = ['user', 'service_name', 'message', 'issue_date']
