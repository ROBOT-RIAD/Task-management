from django.shortcuts import render,redirect
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializer


class ActivateUserView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return redirect("http://localhost:3000/login")
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return Response({'message': 'Activation link is invalid!'}, status=400)