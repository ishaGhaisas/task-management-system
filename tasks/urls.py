from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('test/', views.test, name='test'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('add/addtask/', views.addtask, name='addtask'),
]