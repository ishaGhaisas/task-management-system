from django.template import loader
from django.http import HttpResponse

def tasks(request):
    template =  loader.get_template('index.html')
    return HttpResponse(template.render())


# Create your views here.
