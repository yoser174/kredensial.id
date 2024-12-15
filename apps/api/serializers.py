from rest_framework import serializers
from django.contrib.auth.models import Group, User
from apps.webapp.models import StatusPermohonan, PermohonanKredensial


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusPermohonan
        fields = ["pk", "name"]


# class PermohonanKredensialSerializer(serializers.HyperlinkedModelSerializer):
#     user = serializers.StringRelatedField(many=False)
#     status = serializers.StringRelatedField(many=False)
#     kepada = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = PermohonanKredensial
#         fields = ["pk", "user", "status", "rincian_kewenangan", "unit_kerja", "kepada"]


class PermohonanKredensialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.StringRelatedField(many=False)
    kepada = serializers.StringRelatedField(many=True)

    class Meta:
        model = PermohonanKredensial
        fields = ("id", "status", "rincian_kewenangan", "unit_kerja", "kepada")
        datatables_always_serialize = ("id",)
