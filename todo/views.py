from django.forms import DateTimeInput
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["deadline"].widget = DateTimeInput(
            attrs={"type": "datetime-local"},
            format="%Y-%m-%dT%H:%M"
        )

        return form


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class ToggleAssignDetailView(generic.DetailView):
    @staticmethod
    def post(request, pk, *args, **kwargs):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo:task-list"))
