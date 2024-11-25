from django.contrib import admin
from django.urls import path

from todos.views import TodolistView, TodoCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodolistView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
]
