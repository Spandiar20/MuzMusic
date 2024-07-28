from django import template
from account.models import Profile
from django.db.models import Count


register=template.Library()



@register.inclusion_tag('account/writer-info.html')
def writer_widget(pid):
    profile=Profile.objects.get(id=pid)
    return {
        'profile':profile
    }
   
   