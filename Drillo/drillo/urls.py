from django.contrib import admin
from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing, name='landing'),
    path('admin/', admin.site.urls),
    path('event/', include('eventman.urls')),
    path('user/', include('user.urls')),
]