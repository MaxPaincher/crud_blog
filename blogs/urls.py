from django.urls import path
from blogs.views import BlogListView, BlogCreateView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/create/", BlogCreateView.as_view(), name="create")
]