
from django.http import HttpResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404 , render

# Create your views here.

def index(request):

    title = "Welcome to Django"

    return render(request,'index.html' ,{
        'title':title,
    })


def hello(request,username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username= "Roger"
    return render(request,'about.html' ,{
        'username':username,
    })

def Projects(request):
    projects = list(Project.objects.values())
    return render(request,'projects.html')


def Tasks(request):
    #task = get_object_or_404(Task, id=id)
    return render(request,'tasks.html')