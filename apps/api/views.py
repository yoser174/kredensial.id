from rest_framework import permissions, viewsets

from apps.api.serializers import PermohonanKredensialSerializer
from apps.webapp.models import PermohonanKredensial


class PermohonanKredensialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = PermohonanKredensial.objects.all().order_by("-id")
    serializer_class = PermohonanKredensialSerializer
    permission_classes = [permissions.IsAuthenticated]
