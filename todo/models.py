from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    class Meta:
        ordering = ["is_done", "-datetime"]

    def __str__(self):
        deadline_str = (
            self.deadline.strftime("%m %d, %I:%M %p")
            if self.deadline
            else "Not deadline"
        )
        return f"{self.content}: {self.datetime.strftime("%m %d, %I:%M %p")}, deadline: {deadline_str}"