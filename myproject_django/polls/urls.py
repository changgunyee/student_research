from django.urls import path
from django.contrib import admin
from . import views

app_name='polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('upload',views.upload,name='upload'),
    path('person/<int:person_id>',views.answers_by_person,name='answers_by_person'),
]

