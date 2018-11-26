from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    path('upload',views.upload,name='upload'),
    path('person/<int:person_id>',views.person,name='person'),
    path('response_rate',views.response_rate,name='response_rate'),
]