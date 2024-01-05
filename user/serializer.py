from rest_framework import serializers
from . import models

class Serializer(serializers.ModelSerializer):
    class Meta:
        # model = models.
        fields = "__all__"