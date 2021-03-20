from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.views import View
from .models import Task
from .forms import TaskForm

# Create your views here.
class Tasks(View):
    
    def get(self, request):
        tasks = Task.objects.all().order_by('-id')
        form = TaskForm()
        return render(request, 'index.html', {'form':form,'tasks':tasks})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return JsonResponse({
                'msg':'success',
                'task':model_to_dict(task)
            })
        else:
            return redirect('/')

class DeleteTask(View):

    def post(self, request):
        task = Task.objects.get(pk=request.POST.get('id'))
        task.delete()
        return JsonResponse({
            'deleted':'deleted'
        })
