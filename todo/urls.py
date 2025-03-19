from django.urls import path

from todo.views import TaskListView, TaskDetailView, TaskDeleteView, TaskCreateView, TaskUpdateView, \
    toggle_assing_to_task

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/toggle-assing", toggle_assing_to_task, name="toggle-task-assing"),
]


app_name = "todo"