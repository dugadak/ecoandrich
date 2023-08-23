# app_name/serializers.py
from rest_framework import serializers

class GPTRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField()

class GPTResponseSerializer(serializers.Serializer):
    response = serializers.CharField()
