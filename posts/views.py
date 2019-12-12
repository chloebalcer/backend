from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import (authentication_classes, permission_classes)


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = ()
    # permission_classes = ()
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

