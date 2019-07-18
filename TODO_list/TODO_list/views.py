from django.http import HttpResponse
from django.shortcuts import render, redirect
from list.models import List
from list import models
from .forms import ListForm
from django.contrib import messages


def login(request):
    return render(request,'login.html')

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,("Task Has Been Added To List!"))
            return render(request,'home.html',{'all_items': all_items})

    else:
        all_items = List.objects.all()
        return render(request,'home.html',{'all_items': all_items})


def delete(request,list_id):
    task = List.objects.get(pk=list_id)
    task.delete()
    messages.success(request,("Task removed!"))
    return redirect('home')

def cross_off(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = True
    task.save()
    return redirect('home')


def uncross(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = False
    task.save()
    return redirect('home')


def edit(request, list_id):
    if request.method=='POST':
        task = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request,("Task Has Been Edited!!"))
            return redirect('home')
    else:
        task = List.objects.get(pk=list_id)
        return render(request,'edit.html',{'task': task})


def register(request):
     if request.method == 'POST':
         x1 = request.POST.get('x1')
         x2 = request.POST.get('x2')
         x3 = request.POST.get('x3')

         x4 = models.register(username=x1,password=x2,email=x3)
         x4.save()
         print(x1,x2,x3)
         if x4:
             return render(request,'Sign_up.html')
     else:
         return render(request,'Sign_up.html')
