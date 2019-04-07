from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.bday, name='bday'),
]