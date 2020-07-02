from django.shortcuts import render
from app.forms import *
# Create your views here.

def Topic(request):
    topicform=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            
    return render(request,'topic_form.html',context={'topicform':topicform})



def webpage(request):
    webpageform=WebpageForm()
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,'webpage_form.html',context={'webpageform':webpageform})

def Access(request):
    accessform=AccessForm()
    if request.method=='POST':
        form_data=AccessForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,'Access_form.html',context={'accessform':accessform})