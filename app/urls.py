from django.urls import path
from .views import TaskCreateAPIView, TaskAssignmentAPIView, UserTasksAPIView,CreateUser

urlpatterns = [
    path("createUser",CreateUser.as_view(),name="create_user"),
    path('tasks/create', TaskCreateAPIView.as_view(), name='create_task'),
    path('tasks/assign', TaskAssignmentAPIView.as_view(), name='assign_task'),
    path('usersViewTask/<int:userId>/tasks', UserTasksAPIView.as_view(), name='user_tasks'),
    path('usersViewTask//tasks', UserTasksAPIView.as_view(), name='user-tasks'),
]