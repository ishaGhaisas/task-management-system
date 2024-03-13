from django.template import loader
from django.http import HttpResponse
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
