from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import Group, User
from apps.webapp.models import StatusPermohonan, PermohonanKredensial


class UserSerializer(serializers.HyperlinkedModelSerializer):
    value = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "value",
            "name",
            "email",
            "avatar",
        ]

    def get_value(self, obj):
        return obj.pk

    def get_name(self, obj):
        if obj.first_name == "":
            return obj.username
        return str(obj.first_name + " " + str(obj.last_name)).strip()

    def get_avatar(self, obj):
        return settings.BASE_URL + "/avatar/render_primary/" + str(obj.pk) + "/40/40"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusPermohonan
        fields = ["pk", "name"]


class PermohonanKredensialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.StringRelatedField(many=False)
    kepada = serializers.StringRelatedField(many=True)

    class Meta:
        model = PermohonanKredensial
        fields = ("id", "status", "rincian_kewenangan", "unit_kerja", "kepada")
        datatables_always_serialize = ("id",)
