from django import forms
from .models import Subject, Topic, About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(email=username).exists():
            return username
        raise forms.ValidationError('No user found with this email.')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name',)

class TopicForm(forms.ModelForm):
    heading = forms.CharField(max_length=100, required=False)  # Add heading field
    points = forms.CharField(widget=forms.Textarea, required=False)  # Add points field

    class Meta:
        model = Topic
        fields = ('name', 'classes', 'subject', 'content', 'image', 'heading', 'points')
    # class Meta:
    #     model = Topic
    #     fields = ('name', 'classes' , 'subject', 'content', 'image')

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('content', 'image', 'right_text')