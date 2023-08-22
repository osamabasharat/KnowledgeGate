from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from knowledgegate.LW.forms import SubjectForm
from .models import Classes, Subject, Topic
from .forms import SubjectForm, TopicForm
def class_list(request):
   classes = Classes.objects.all()
   return render(request, 'LW/class_list.html', {'classes' : classes})

def subject_list(request, class_id):
    classes = Classes.objects.get(pk=class_id)
    subjects = Subject.objects.filter(classes=classes)
    return render(request, 'LW/subject_list.html', {'classes': classes, 'subjects': subjects})

def topic_list(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    topics = Topic.objects.filter(subject=subject)
    return render(request, 'LW/topic_list.html', {'subject': subject, 'topics': topics})

def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('LW:topic_list', subject_id=form.cleaned_data['subject'].id)
    else:
        form = TopicForm()
    return render(request, 'LW/add_topic.html', {'form': form})


def add_subject(request, class_id):
    classes = Classes.objects.get(pk=class_id)

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.classes = classes
            subject.save()
            return redirect('add_topic', class_id=class_id, subject_id=subject.id)
    else:
        form = SubjectForm()

    return render(request, 'classes/add_subject.html', {'form': form, 'classes': classes})



def index(request):
   return render(request, "LW/index.html",)

# Create your views here.
def SignupPage(request):
   return render(request, 'Signup.html')

def LoginPage(request):
   return render(request, 'Login.html')

