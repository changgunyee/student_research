from django.urls import include,path
from . import views

app_name='polls'
urlpatterns = [
    path('upload',views.upload),
    path('person/page/',include([
        path('<int:current_page>/',views.person_by_page),
        path('<int:current_page>-<int:num>',views.person_by_page),
    ])),
    path('person/page/',include([
        path('<int:current_page>/',views.answer_rate_by_page),
        path('<int:current_page>-<int:num>',views.answer_rate_by_page),
    ])),
]