from django import template
from account.models import Profile
import random
from utils import follow_unfollow


register=template.Library()

@register.inclusion_tag('website/profiles_website.html')
def blog_profiles():
    profiles=list(Profile.objects.all())
    random.shuffle(profiles)
    try:
        profiles=profiles[:10]
    except:
        pass   
    return {
        'random_profiles':profiles
    }