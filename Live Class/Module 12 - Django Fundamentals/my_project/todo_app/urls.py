from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'), 
    path('<int:pk>/', views.task_details, name='task_details'), 
    path('add_task/', views.add_task, name='add_task'), 
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'), 
    path('update_task/<int:pk>/', views.update_task, name='update_task'), 
    path('add_task_form/', views.add_task_form, name='add_task_form'), 

] 