from django.urls import path
from .views import register_user

app_name='account'

urlpatterns = [
    path('register/',register_user,name='register')
   
]
