from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create-contact/', views.create_contact, name='create-contact'),
]