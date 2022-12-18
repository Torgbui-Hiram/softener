from django.urls import path
from . import views


urlpatterns = [
    path('mess_to', views.send_message, name='send_mess')
]
