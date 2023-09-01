"""
URL configuration for knowledgegate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from LW import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("LW/", include("LW.urls")),
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("login/", views.login_view , name="login"),
    path('signup/', views.signup, name='signup'),
    path('classes/', views.class_list, name='class_list'),
    # path('subjects/<int:subject_id>/chapters/', views.chapter_list, name='subject_chapters'),
    # path('chapters/<int:chapter_id>/topics/', views.topic_list, name='chapter_topics'),
    path('classes/<int:class_id>/subjects/', views.subject_list, name='subject_list'),
    path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topics/add/', views.add_topic, name='add_topic'),
    path('tinymce/', include('tinymce.urls')),
    path('', views.home, name='home'),
    #path('about/', views.about, name='about'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('faqs/', views.faq_list, name='faqs'),
    # path('faq/', views.faqs, name='faqs'),
    path('catalogue/<int:class_id>/', views.class_detail, name='class_detail'),
    path('about/', views.about_view, name='about'),
  
    # path('classes/', views.class_list, name='class_list'),
    # path('classes/<int:class_id>/subjects/', views.subject_list, name='subject_list'),
    # path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    # path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    # path('topics/add/', views.add_topic, name='add_topic'),
    # path('', views.SignupPage, name='signup'),
    # path('Login/', views.LoginPage, name='Login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

