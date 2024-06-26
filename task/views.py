from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from task.models import Tag, Task


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tag_list"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    context_object_name = "task_list"
