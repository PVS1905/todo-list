from django.urls import path

from todo.views import (
    TaskListView,
    TaskDetailView,
    TaskDeleteView,
    TaskCreateView,
    TaskUpdateView,
    toggle_assign_to_task,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    TagDetailView
)

# urlpatterns = [
#     path("", TaskListView.as_view(), name="task-list"),
#     path("task/create", TaskCreateView.as_view(), name="task-form"),
#     path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
#     path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
#     path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
#     path("task/<int:pk>/toggle-assing", toggle_assign_to_task, name="toggle-task-assign"),
#     path("tags/", TagListView.as_view(), name="tag-list"),
#     path("tags/create", TagCreateView.as_view(), name="tag-form"),
#     path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
#     path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
# ]

urlpatterns = [
    # path("", index, name="index"),
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-form"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-form"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path(
        "task/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),

]
app_name = "todo"