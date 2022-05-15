from .models import Accounts
from .serializers import PostSerializer
from accounts import serializers
from rest_framework.viewsets import ModelViewSet


class Accounts(ModelViewSet):
    model = Post
    serializer_class = AccountsSerializer
    queryset= Post.objects.all()
