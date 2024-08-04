from django import template
from account.models import Profile
from django.db.models import Count
from django.contrib.auth.models import User


register=template.Library()



# @register.inclusion_tag('account/writer-info.html')
# def writer_widget(username):
#     profile=Profile.objects.get(user__username=username)
#     return {
#         'profile':profile
#     }
   
   # this tag is only used when you go to a 

