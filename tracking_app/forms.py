from django import forms
from tracking_app.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status', 'priority', 'date']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
class TaskFilterForm(forms.Form):
    STATUS = [
        ("", "all"),
        ("todo", "Need to do"),
        ("in_progress", "In Development"),
        ("completed", "Completed"),
    ]
    
    PRIORITY = [
        ("", "all"),
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    status = forms.ChoiceField(choices=STATUS, required=False, label="Статус")
    priority = forms.ChoiceField(choices=PRIORITY, required=False, label="Приоритет")