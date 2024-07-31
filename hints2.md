**wierd error**

Page not found (404)
“D:\Programming\NewMuzMusic\media\account\register” does not exist

problem solver in the settings
MEDIA_URL = '/media/'


# Mordad 9th 1:30 am

follow and unfollow
```html

<div class="button-group-area mt-10">
        <form method="POST">
            {% csrf_token %}
            {% if profile in user.profile.follows.all %}
                <button href="#" name="follow" type="submit" value="unfollow" class="genric-btn success-border medium">Following</button>
            {% else %}	
                <button href="#" value="follow" name="follow" type="submit" class="genric-btn success-border medium">Follow</button>

            {% endif %}
        </form>
    </div>
```






# follwing and unfollowing
```python 

def members_profile(request):
    profiles=Profile.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_user_profile=request.user.profile
            action=request.POST['follow']
            target_profile=request.POST['target_profile']
            if action == 'unfollow':
                current_user_profile.follows.remove(target_profile)
            else:
                current_user_profile.follows.add(target_profile)
            current_user_profile.save()    
    return render(request,'account/members.html',{
        'profiles':profiles
    })






```


# Mordad 9th 10 am
**just added the like button**





# Big Question
**when to use a form and when to use an a tag??**



# Mordad 9th 1:00 pm
now im going to work on the personal pages of the users
so i need a new template lets say blog-author.html



# Mordad 9th 6:00 pm
the problem is the  page of each user, in this page you can see the psots of a particular user and all the related info to the user, 
Actually i have difficulties accessing both posts and the specific profile.
i have to access the profile from the user
 blog/author/<str:author_name> 

**2 hours later , ihad a typo! its done**


# lets make the follow button a custom tag 
i think its a good approach to make it reusable
**Mordad 9th 8:00 pm**
the above approach is not gonna work , well two ways available 
1- make the following button an a tag so that using herf you can send the data to the same place
2- use the exising form and diefine two views for following
im lazy lets do the second approach


# Question
for the functions which do not really provide a template , for example a likeView , how should we set a url ? 
```python

    path('single-view/<int:pk>',BlogSingleView.as_view(), name='single_view'),

    path('single-view/<int:pk>',likeView, name='like_post'),

# i did this and the server stops when clicking on the like button!!!!!!!!!!!!!!!!!!!!!!!
```