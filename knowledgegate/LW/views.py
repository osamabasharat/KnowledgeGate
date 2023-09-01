from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from knowledgegate.LW.forms import SubjectForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .models import Classes, Subject, Topic, FAQ, About
from .forms import CustomUserCreationForm, EmailAuthenticationForm, SubjectForm, TopicForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
#from .models import FAQ


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



# def chapter_list(request, subject_id):
#     subject = Subject.objects.get(pk=subject_id)
#     chapters = Chapter.objects.filter(subject=subject)
#     return render(request, 'LW/chapter_list.html', {'subject': subject, 'chapters': chapters})


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

def topic_detail(request, topic_id):
       selected_topic = get_object_or_404(Topic, id=topic_id)
       print(selected_topic.pdf_file)
       return render(request, 'LW/topic_detail.html', {'selected_topic': selected_topic})
       #return render(request, 'topic_detail.html', {'topic': topic, 'exercises': exercises})
       
    # selected_topic = get_object_or_404(Topic, id=topic_id)
    # context = {'selected_topic': selected_topic}
    # return render(request, 'topic_detail.html', context)


def about_view(request):
    about_info = About.objects.first()  # Assuming you have only one about info
    context = {'about_info': about_info}
    return render(request, 'LW/about.html', context)
# def about(request):
#     about_info = About.objects.all()
#     return render(request, 'LW/about.html', {'about_info': about_info})

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'LW/faq.html', {'faqs': faqs})

def index(request):
   return render(request, "LW/index.html",)
def home(request):
    return render(request, 'LW/home.html')

# def about(request):
#     return render(request, 'LW/about.html')

def catalogue(request):
    classes = Classes.objects.all()
    return render(request, 'LW/catalogue.html', {'classes': classes})

# def faqs(request):
#     return render(request, 'LW/faq.html')
def class_detail(request, class_id):
    # Retrieve the class object based on class_id
    selected_class = Classes.objects.get(pk=class_id)
    return render(request, 'LW/class_detail.html', {'selected_class': selected_class})
# Create your views here.
# def SignupPage(request):
#    return render(request, 'Signup.html')

# def LoginPage(request):
#    return render(request, 'Login.html')
class CustomLoginView(LoginView):
    template_name = 'LW/Login.html'
    authentication_form = EmailAuthenticationForm

    def form_valid(self, form):
        """Override form_valid to add success message and redirect."""
        messages.success(self.request, 'You have successfully logged in.')
        return super().form_valid(form)

def login_view(request):
    return CustomLoginView.as_view()(request)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after signup
            login(request, user)
            messages.success(request, 'You have successfully signed up and logged in.')
            return redirect('index')  # Replace with your desired redirection
    else:
        form = CustomUserCreationForm()
    return render(request, 'LW/Signup.html', {'form': form})

# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')  # Replace 'home' with your desired redirection
#         else:
#             # Invalid credentials
#             error_message = 'Invalid username or password.'
#     else:
#         error_message = ''

#     return render(request, 'LW/Login.html', {'error_message': error_message})


# def signuppage(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Log the user in after signup
#             login(request, user)
#             return redirect('login')  # Replace with your desired redirection
#     else:
#         form = UserCreationForm()
#     return render(request, 'LW/Signup.html', {'form': form})

# def exercise_pdf_view(request, exercise_id):
#     exercise = get_object_or_404(Exercise, id=exercise_id)
#     with open(exercise.pdf_file.path, 'rb') as pdf_file:
#         response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#         response['Content-Disposition'] = f'inline; filename="{exercise.name}.pdf"'
#         return response

