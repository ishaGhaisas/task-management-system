from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks

def tasks(request):
    myTasks = Tasks.objects.all().values()
    template =  loader.get_template('allTasks.html')
    context = {
        'myTasks' : myTasks
    }
    return HttpResponse(template.render(context, request))


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def test(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())

def delete(request, id):
  task = Tasks.objects.get(id=id)
  task.delete()
  return HttpResponseRedirect(reverse('tasks'))

def add(request):
  template = loader.get_template('addTask.html')
  return HttpResponse(template.render({}, request))

def addtask(request):
  taskName = request.POST['taskName']
  description = request.POST['description']
  due_date = request.POST['due_date']
  priority = request.POST['priority']
  status = request.POST['status']
  task = Tasks(taskName=taskName, description=description, due_date=due_date, priority=priority, status=status)
  task.save()
  return HttpResponseRedirect(reverse('tasks'))