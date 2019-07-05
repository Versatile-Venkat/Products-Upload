from django.conf.urls import include
from django.urls import path
from reg import views
urlpatterns=[
    path('api/',views.RegistrationList.as_view()),
]