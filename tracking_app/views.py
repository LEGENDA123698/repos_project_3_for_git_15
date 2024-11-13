from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from tracking_app.models import *
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from tracking_app.mixins import UserIsOwnerMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class MainScreenView(ListView):
    model = Tasks
    template_name = 'main_screen.html'



class DoTaskListView(ListView):
    model = Tasks
    template_name = 'boards/DO/do_task_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        priority = self.request.GET.get("priority", "")

        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)
        return context
        
        

        
    
class DoTaskDetailView(DetailView):
    model = Tasks
    template_name = 'boards/DO/do_task_detail.html'
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        form.instance.author = request.user
        form.instance.task = self.get_object()
        
        if form.is_valid():
            form.save()
            return redirect('do-task-detail',  pk = self.get_object().pk)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(task=self.get_object())
        context["form"] = CommentForm()
        return context
    
    
class ChangeStatusView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        change = self.get_object()

        if change.status == 'todo':
            change.status = 'in_progress'
            
        elif change.status == 'in_progress':
            change.status = 'completed'
            
        else:
            print("Неможливо змінити статус.")

        change.save()
        return HttpResponseRedirect('/task-list')
    
    def get_object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(Tasks, pk=task_id)
    
    
class ChangePriorityView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        change = self.get_object()

        if change.priority == 'low':
            change.priority = 'medium'
            
        elif change.priority == 'medium':
            change.priority = 'high'
            
        else:
            print("Неможливо змінити пріорітет.")

        change.save()
        return HttpResponseRedirect('/task-list')
    
    def get_object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(Tasks, pk=task_id)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = '/task-list'
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Tasks
    template_name = 'update_task_view.html'
    form_class = TaskForm
    success_url = '/task-list'

class CommentUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Comment
    template_name = 'update_comm_view.html'
    form_class = CommentForm
    success_url = '/task-list'

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Tasks
    template_name = 'delete_task_view.html'
    success_url = '/task-list'

class CommentDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Comment
    template_name = 'delete_comm_view.html'
    success_url = '/task-list'  
    
def login_user(request):
    if request.method == 'POST':
        form = UserAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main-page')
            else:
                messages.error(request, 'invalid login or password')
    else:
        form = UserAuthForm()

    return render(request, 'account_settings/login.html', context = {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main-page')
        else:
            print("FormnotVakid")
    else:
        form = UserCreateForm()

    return render(request, 'account_settings/register.html', context = {'form': form})

