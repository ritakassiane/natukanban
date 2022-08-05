from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Column, Task
from .forms import AddTask, EditTaskForm

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
    
    column_status_dict = title_to_dict(column_list)
    tasks_ = {}
    for title, tasks in column_status_dict.items():
        column_status_dict[title]=(Task.objects.filter(status__title=title))
        print(f'TITULO{title}')
        print("")
        print("#############")
    print(column_status_dict)
    tasks_ = column_status_dict
    # tasks_ = {'In progress' : Task.objects.filter(status__title="In progress"),
    # 'To do':Task.objects.filter(status__title="To do"),
    # 'Do today':Task.objects.filter(status__title="Do Today"),
    # 'Done':Task.objects.filter(status__title="Done")}
    print(tasks_)
    


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

    return render(request, 'board/main_board.html', 
    {'main_board':main_board, 
    'columns': columns, 
    'tasks':tasks, 
    'task_in_progress':task_in_progress, 
    'task_to_do': task_to_do, 
    'task_done': task_done, 
    'task_do_today': task_do_today, 
    'tasks_':tasks_,
    'form':form,
    })

def done_task(request, task_id):
    tarefa = get_object_or_404(Task, id=task_id)
    status_ = Column.objects.get(title='Done')
    tarefa.status = status_
    tarefa.save()
    return redirect('board_main')

def delete_task(request, task_id):
    tarefa = get_object_or_404(Task, id=task_id)
    tarefa.delete()
    return redirect('board_main')

def edit_task(request, task_id):
    tarefa = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = EditTaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.description = cd['description']
            tarefa.category = cd['category']
            tarefa.title = cd['title']
            tarefa.save()
            return redirect('board_main')
    else:
        form = EditTaskForm(initial={'task':tarefa.description, 'category':tarefa.category, 'title':tarefa.title})
    return render(request, 'board/edit_task.html', {'task':tarefa, 'form':form})