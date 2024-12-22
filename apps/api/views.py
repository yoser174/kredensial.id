from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from apps.api.serializers import PermohonanKredensialSerializer, UserSerializer
from apps.webapp.models import PermohonanKredensial


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermohonanKredensialViewSet(viewsets.ModelViewSet):
    queryset = PermohonanKredensial.objects.all().order_by("-id")
    serializer_class = PermohonanKredensialSerializer
    permission_classes = [permissions.IsAuthenticated]
