from django.urls import path
from tracking_app import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('register', views.register, name = "register"),
    path('main-page', views.MainScreenView.as_view(), name = "main-page"),
    path('task-list', views.DoTaskListView.as_view(), name = "do-task-list"),
    path('task/<int:pk>/', views.DoTaskDetailView.as_view(), name = "do-task-detail"),
    path('<int:pk>/update_task/', views.TaskUpdateView.as_view(), name = "task-update"),
    path('<int:pk>/delete_task/', views.TaskDeleteView.as_view(), name = "task-delete"),
    path('<int:pk>/update_comm/', views.CommentUpdateView.as_view(), name = "comm-update"),
    path('<int:pk>/delete_comm/', views.CommentDeleteView.as_view(), name = "comm-delete"), 
    path('add-note', views.TaskCreateView.as_view(), name = "note-add-create"),
    path('<int:pk>/change_status/', views.ChangeStatusView.as_view(), name = "change-status"),
    path('<int:pk>/change_priority/', views.ChangePriorityView.as_view(), name = "change-priority"),
    path('logout/', views.logout_view, name="logout"),
]
