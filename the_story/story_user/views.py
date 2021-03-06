from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import permissions
from oauth2_provider.contrib.rest_framework.permissions import TokenHasReadWriteScope, TokenHasScope
from rest_framework import viewsets, generics

from story_user.serializer import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
