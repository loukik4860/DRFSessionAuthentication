from django.shortcuts import render
from django.utils.encoding import force_str, force_bytes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from .models import User
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from .utils import send_activation_email


# Create your views here.

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            # Send Account Activation Email
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse('activate', kwargs={'uid': uid, 'token': token})
            activation_url = f"{settings.SITE_DOMAIN}{activation_link}"
            send_activation_email(user.email, activation_url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
