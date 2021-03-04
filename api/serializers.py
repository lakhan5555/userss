from rest_framework import serializers
from .models import Userss

class UserssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userss
        fields = "__all__"
        