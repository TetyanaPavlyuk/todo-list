from django.urls import path

from .views import TagListView, TaskListView


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "task"
