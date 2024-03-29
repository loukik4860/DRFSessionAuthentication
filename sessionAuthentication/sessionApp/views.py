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

@method_decorator(ensure_csrf_cookie,name='dispatch')
class getCSRFToken(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        return Response({'success':'csrf Cookies set'})

@method_decorator(csrf_protect,name='dispatch')
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

@method_decorator(csrf_protect,name='dispatch')
class ActivateView(APIView):
    permission_classes = [AllowAny]

@method_decorator(csrf_protect,name='dispatch')
class Activation_Confirm(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')

        if not uid or not token:
            return Response({'detail': 'missing uid or token'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                if user.is_active:
                    return Response({'details': 'Account is aready Activated'}, status=status.HTTP_200_OK)
                user.is_active = True
                user.save()
                return Response({'detail': 'Account activated Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'details': 'Invalid Activation link'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'details': 'Invalid activation link'}, status=status.HTTP_400_BAD_REQUEST)
