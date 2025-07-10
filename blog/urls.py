from django.urls import path
from . import views
from .views import PostListView ,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView


urlpatterns = [
    # path('', views.home , name= "Blog-Home"),
    path('' , PostListView.as_view() , name = 'Blog-Home'),
    path('post/<int:pk>/' , PostDetailView.as_view() , name = 'post_view'),
    path('post/new/' , PostCreateView.as_view() , name = 'post_create'),
    path('post/<int:pk>/update/' , PostUpdateView.as_view() , name = 'post_update'),
    path('post/<int:pk>/delete/' , PostDeleteView.as_view() , name = 'post_delete')


]