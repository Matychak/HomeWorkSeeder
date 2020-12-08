from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('404', views.error_page, name='error_page'),
]
