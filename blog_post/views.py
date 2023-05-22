from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from . import models
from .serializers import PostListSerializer, PostCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostListCreate(generics.ListCreateAPIView):
    queryset = models.BlogPostModel.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = PostListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = models.BlogPostModel.objects.all()
    serializer_class = PostListSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = models.BlogPostModel.objects.all()
    serializer_class = PostCreateSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = models.BlogPostModel.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BlogPostModel.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return PostCreateSerializer
        return PostListSerializer
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
