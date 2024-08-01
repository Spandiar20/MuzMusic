from django.shortcuts import render
from account.models import Profile
import random
from utils import follow_unfollow


from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.models import Profile
from blog.forms import FollowForm
from utils import follow_unfollow

# @method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch random profiles to display
        if self.request.user.is_authenticated:
            context['random_profiles'] = Profile.objects.exclude(user=self.request.user).order_by('?')
        else:
            context['random_profiles'] = Profile.objects.all().order_by('?')
   
        context['follow_form'] = FollowForm()
        return context
    
    @login_required
    def post(self, request, *args, **kwargs):
        form = FollowForm(request.POST)
        if form.is_valid():
            target_profile_id = form.cleaned_data['target_profile_id']
            current_user_profile = request.user.profile  # Assuming there's a one-to-one relation
            target_profile = Profile.objects.get(id=target_profile_id)
            follow_unfollow(current_user_profile, target_profile)
            # sometimes i dont understand difference between the obj and its id
            return redirect('website:index')  # Redirect back to the index page

        return self.get(request, *args, **kwargs)
# im kinda feeling code smell for habdling the unuthorized user in the index page
# i am adding condidtions for the rando_profiles and i am creating a fake follow buttom
# for the unauthorized user to be taken to the login page