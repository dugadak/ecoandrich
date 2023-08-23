# app_name/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import GPTRequestSerializer, GPTResponseSerializer
import openai
from django.conf import settings

class GPTViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = GPTRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prompt = serializer.validated_data['prompt']

        if not prompt:
            raise ValidationError("Prompt cannot be empty.")

        openai.api_key = settings.OPENAI_API_KEY
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=3000
            )
        except openai.error.OpenAIError as e:
            return Response(
                {"error": "Error while processing the request."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        gpt_response = {
            "response": response.choices[0].text
        }
        response_serializer = GPTResponseSerializer(gpt_response)
        return Response(response_serializer.data, content_type='application/json')

