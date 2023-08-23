from django.urls import path
from . import views
app_name = "LW"
urlpatterns = [
    path("", views.index, name="index"),
    path('classes/', views.class_list, name='class_list'),
    path('classes/<int:class_id>/subjects/', views.subject_list, name='subject_list'),
    path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topics/add/', views.add_topic, name='add_topic'),
]
