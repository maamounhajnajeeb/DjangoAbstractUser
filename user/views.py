from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from user.models import AdminProfile


class AdminProfileSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = AdminProfile


class AdminProfileViews(ModelViewSet):
    serializer_class = AdminProfileSerializer
    queryset = AdminProfile.objects.all()
