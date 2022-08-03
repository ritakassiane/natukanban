from django.shortcuts import render, redirect
from .models import Board, Column, Task

def board_main(request):
    main_board = Board.objects.all()
    columns = Column.objects.all()
    tasks = Task.objects.all()
    # tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    return render(request, 'board/main_board.html', {'main_board':main_board, 'columns': columns, 'tasks':tasks})

