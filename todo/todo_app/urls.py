from django.urls import path
from todo_app import views

urlpatterns = [
    path('tags/', views.get_tags, name='get_tags')
]