from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from .models import task
from . import forms
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# Create your views here.
def index(request):
	Date = datetime.datetime.now()
	Tasks = task.objects.all()

	if len(list(Tasks)) == 0:
		Tasks = None
	else:
		Tasks = list(Tasks.values().filter(completed=False).order_by('priority', '-due_time', '-due_date', 'title'))

	return render(request, 'todo/index.html', {
		'new_task': forms.newTask,
		'year': Date.strftime('%Y'),
		'today': f"{Date.strftime('%A')}, {Date.strftime('%B')} {Date.strftime('%d')}",
		'task': Tasks
	})


def add(request):
	if request.method == 'POST':
		form = forms.newTask(request.POST)

		if form.is_valid():
			Task = form.save(commit=False)
			Task.priority = 3 if Task.priority == '' else Task.priority
			Task.completed = False
			Task.save()
			return redirect('/')

	else:
		form = forms.newTask()

	return redirect('index')


def complete(request):
	if request.method == 'POST':
		task_id = request.POST["task_id"]

		Task = task.objects.get(id=task_id)
		Task.completed = True
		Task.completed_on = timezone.now()
		Task.save()

		logging.info(f"{Task} completed!")

	else:
		pass

	return redirect('index')
