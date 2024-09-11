from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class todoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todolist", null=True
    )  # on cascade deletes item if todolist is deleted
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class item(models.Model):
    todoList = models.ForeignKey(
        todoList, on_delete=models.CASCADE
    )  # on cascade deletes item if todolist is deleted
    text = models.CharField(max_length=300)  # task discription
    complete = models.BooleanField()

    def __str__(self):
        return self.text
