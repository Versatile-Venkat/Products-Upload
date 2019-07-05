from django.conf.urls import include
from django.urls import path
from sup import views
urlpatterns=[
    path('api/',views.SupplierList.as_view()),
]