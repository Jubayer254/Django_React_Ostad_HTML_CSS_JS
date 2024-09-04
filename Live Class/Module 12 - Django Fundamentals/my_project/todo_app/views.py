from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == '1':
        tasks = tasks.filter(completed = True)
    elif completed == '0':
        tasks = tasks.filter(completed = False)
    return render(request, 'task_list.html', {"tasks": tasks})

def task_details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')

    return render(request, 'task_details.html', {"task": task})

def add_task(request):
    _title = 'test'
    _description = 'test'
    _completed = True
    _due_date = "2024-08-28"
    task = Task(title=_title, description=_description, completed=_completed, due_date = _due_date)
    task.save()
    return redirect(task_list)

def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')
    return redirect(task_list)

def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.title = 'Updated'
        task.save()
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')
    return redirect(task_list)

def add_task_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        # if form.is_valid() and form.cleaned_data["age"] > 150:
        if form.is_valid(): 
            form.save()
            return redirect(task_list)
        else:
            return render(request, 'add_task.html', {"form": form})

    else:
        form = TaskForm()
        return render(request, 'add_task.html', {"form": form})
    
def update_task_form(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        if request.method == 'POST':
            task_form = TaskForm(request.POST, instance=task)
            if task_form.is_valid(): 
                task_form.save()
                return redirect(task_list)
            else:
                return render(request, 'update_task.html', {"form": task_form})
        

        task_form = TaskForm(instance=task)
        return render(request, 'update_task.html', {"form": task_form})
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')