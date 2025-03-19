from django.forms import DateTimeInput
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"


class TaskDetailView(generic.DetailView):
    model = Task
    fields = "__all__"



class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["deadline"].widget = DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M")
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
    model = Task
    fields = "__all__"


def toggle_assing_to_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))

