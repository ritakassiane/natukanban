from django.shortcuts import render, redirect
from .models import Board, Column, Task
from .forms import AddTask

def title_to_dict(title_list):
    result = {}
    for title in title_list:
        result.setdefault(title, [])
    return result

def board_main(request):
    main_board = Board.objects.all()
    columns = Column.objects.all()
    column_list = []

    for column in columns:
        column_list.append(column.title)
    print(title_to_dict(column_list))

    # tasks_ = {'In progress' : Task.objects.filter(status__title="In progress"),
    # 'To do':Task.objects.filter(status__title="To do"),
    # 'Do today':Task.objects.filter(status__title="Do Today"),
    # 'Done':Task.objects.filter(status__title="Done")}
    
    # print(tasks_)

    task_in_progress = Task.objects.filter(status__title="In progress")
    task_to_do = Task.objects.filter(status__title="To do")
    task_do_today = Task.objects.filter(status__title="Do Today")
    task_done = Task.objects.filter(status__title="Done")
    tasks = Task.objects.all()
    # tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    if request.method == 'POST':
        form = AddTask(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_main')
    else:
        form = AddTask()

    return render(request, 'board/main_board.html', {'main_board':main_board, 'columns': columns, 'tasks':tasks, 'task_in_progress':task_in_progress, 'task_to_do': task_to_do, 'task_done': task_done, 'task_do_today': task_do_today, 'form':form})

