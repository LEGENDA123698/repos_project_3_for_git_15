from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model): 
    STATUS = [
        ("todo", "Need to do"),
        ("in_progress", "In Development"),
        ("completed", "Completed"),
    ]
    
    PRIORITY = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY, default="low")
    date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    task = models.ForeignKey(Tasks, related_name="task", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
