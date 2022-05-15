from .models import Post
from rest_framework.serializers import ModelSerializer

class AccountsSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"