from django.urls import path
from .views import register_user,logout_user,login_user,edit_profile,members_profile,bio

app_name='account'

urlpatterns = [
    path('signup',register_user,name='register'),
    path('logout',logout_user,name='logout'),
    path('login/',login_user,name='login'),
    path('edit',edit_profile,name='edit_profile'),
    path('members',members_profile,name='members'),
    path('signup/bio/<str:username>',bio,name='bio')


]
