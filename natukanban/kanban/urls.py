from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.board_main, name='board_main' ),
    path('<int:task_id>/concluir/', views.done_task, name='done_task'),
]