from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from blog import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class PostView(ModelViewSet):
    model = Post
    serializer_class = PostSerializer
    queryset= Post.objects.all()
    permission_classes = [IsAuthenticated]
    


def home(request):

    all_posts = Post.objects.all()

    return render ( request, {'posts' : all_posts })

