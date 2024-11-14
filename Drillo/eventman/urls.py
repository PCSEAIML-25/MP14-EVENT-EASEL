from django.urls import path
from .views import *

urlpatterns = [
    path('create', form_submission, name='form_submission'),
    path('<slug:url>/', page_preview, name='page_preview'),
    path('register/<str:event>', register, name='register'),
    path('event_details/<str:event>', event_details_page, name='event_details'),
]