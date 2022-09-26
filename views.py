from django.shortcuts import render, redirect
from .models import Todolist

# Create your views here.
def index(request):
    todolist=Todolist.objects.all()
    if request.method == 'POST':
        new_todolist= Todolist( 
            title= request.POST['title']
            )
        new_todolist.save()
        return redirect('/')
    return render (request, 'index.html',{'todolists':todolist})

def delete(request,pk):
    todolist=Todolist.objects.get(id=pk)
    todolist.delete()
    return redirect('/')