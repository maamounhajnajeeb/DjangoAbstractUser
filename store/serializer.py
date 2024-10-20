from rest_framework import serializers

from .models import Bolg


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bolg
        fields = "__all__"
