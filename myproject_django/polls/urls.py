from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    path('upload',views.upload),
    path('person/page/<int:current_page>',views.person_by_page),
    path('answer_rate',views.answer_rate),
]