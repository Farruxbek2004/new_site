from django.urls import path

from .views import (
    PostListCreate,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostRetrieveView

)

urlpatterns = [
    path("", PostListCreate.as_view(), name="post_list_create"),
    path("<int:pk>/", PostRetrieveView.as_view(), name="post_read"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    # path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    # path('users/', UserList.as_view(), name='users_list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='users_detail'),
]
