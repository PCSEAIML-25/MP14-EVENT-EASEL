from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('login', views.login, name="login_view"),
    path('logout', views.logout, name="logout_view"),
    path('signup', views.signup, name="signup_view"),
    path('dashboard', views.dashboard, name="dashboard"),
]
