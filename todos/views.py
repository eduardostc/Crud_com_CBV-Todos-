from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import Todo


class TodolistView(LoginRequiredMixin, ListView):
    model = Todo
    login_url = "/auth/login/"  # Redireciona para a página de login se não autenticado


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
    

#parte de login: https://www.youtube.com/watch?v=gdhiA6wObw0

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()

        if user:
            messages.error(request, 'Já existe um usuário com esse username.')
            return render(request, 'cadastro.html')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso! Faça login para continuar.')
        return redirect('login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return redirect("todo_list")
        else:
            messages.error(request, 'Usuário ou senha inválido!')
            return render(request, 'login.html')
        

def logout_view(request):
    logout(request)
    return redirect('/auth/login/')

# @login_required(login_url="/auth/login/")
# def plataforma(request):
#     # if request.user.is_authenticated:
#     #     return HttpResponse('plataforma')
#     return HttpResponse("plataforma")
#     #return redirect('todo_list')