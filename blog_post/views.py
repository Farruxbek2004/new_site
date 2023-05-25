from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPostModel, LikeDislike
from paginations import CustomPageNumberPagination
from .serializers import PostListSerializer, PostCreateSerializer, LikeDislikeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostListCreate(generics.ListCreateAPIView):
    queryset = BlogPostModel.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = PostListSerializer
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = BlogPostModel.objects.all()
    serializer_class = PostListSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = BlogPostModel.objects.all()
    serializer_class = PostCreateSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = BlogPostModel.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPostModel.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return PostCreateSerializer
        return PostListSerializer


class LikeDislikeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=LikeDislikeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        type_ = serializer.validated_data.get("type")
        post = BlogPostModel.objects.filter(id=self.kwargs.get("pk")).first()
        if not post:
            raise Http404
        like_dislike_blog = LikeDislike.objects.filter(post=post, user=user).first()
        if like_dislike_blog and like_dislike_blog.type == type_:
            like_dislike_blog.delete()
        else:
            LikeDislike.objects.update_or_create(post=post, user=user, defaults={"type": type_})

        return Response({"type": type_, "detail": "Liked or disliked."})
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
