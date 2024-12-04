from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from todos.views import TodolistView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", TodolistView.as_view(), name="todo_list"),
    path("", RedirectView.as_view(url="/auth/login/")),  # Redireciona para login
    path("todo/", TodolistView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    path("auth/", include('todos.urls')),
]
