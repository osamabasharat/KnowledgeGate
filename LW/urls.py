from django.urls import path
from . import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this

app_name = "LW"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view , name="login"),
    path('signup/', views.signup, name='signup'),
    path('classes/', views.class_list, name='class_list'),
    path('classes/<int:class_id>/subjects/', views.subject_list, name='subject_list'),
    path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topics/add/', views.add_topic, name='add_topic'),
    path('', views.home, name='home'),
    #path('about/', views.about, name='about'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('faqs/', views.faq_list, name='faqs'),
    path('catalogue/<int:class_id>/', views.class_detail, name='class_detail'),
    path('about/', views.about_view, name='about'),
    #path('exercise_pdf/<int:exercise_id>/', views.exercise_pdf_view, name='exercise_pdf_view'),
    #path('tinymce/', include('tinymce.urls')),
    # path("login/", views.login_view , name="login"),
    # path('signup/', views.signup, name='signup'),
    # path('classes/', views.class_list, name='class_list'),
    # path('classes/<int:class_id>/subjects/', views.subject_list, name='subject_list'),
    # path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    # path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    # path('topics/add/', views.add_topic, name='add_topic'),
] 