from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView




def demo(request):
    tasks = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'task.html',{'task':tasks})
def details(request):

    return render(request,'details.html',)
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'tasks':task})

class Tasklistview(ListView):
    model=Task
    template_name='task.html'
    context_object_name ='task'

class Taskdetailview(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'tasks'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'edits.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object})
class Taskdeleteview(DeleteView):
    model= Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvtask')




def update(request,id):
    task=Task.objects.get(id=id)
    fo=TodoForm(request.POST or None,instance=task)
    if fo.is_valid():
        fo.save()
        return redirect('/')
    return render(request,'edit.html',{'f':fo,'tasks':task})




