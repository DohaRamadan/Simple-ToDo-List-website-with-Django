from django.urls import path
from .views import *
from .models import * 
from django.contrib.auth.views import LogoutView


app_name = 'base'
urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page= 'base:login'), name='logout'), 
    path('signup', RegisterPage.as_view(), name="signup"), 
    path('', TaskList.as_view(), name='tasks'), 
    path('create-task', TaskCreate.as_view(), name='create-task'), 
    path('update-task/<int:pk>', TaskUpdate.as_view(), name="update-task"), 
    path('delete-task/<int:pk>', TaskDelete.as_view(), name="delete-task"), 
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
]
