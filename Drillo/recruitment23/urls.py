from django.urls import path
from . import views

urlpatterns = [
    path('', views.forms, name="forms"),
    path('submitted/', views.submit, name="submit")
]
