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



# i wasnt able to make the custom login_url for login_reuired decorator
So i changed the url of the login view to accounts/login from account/login and 
the problem was solved!


# now i want to make the following func work!






# registration form
**Mordad 11th 1:00 am**

first the user inputs some data to register then before going to the index he goes to another page for the profile form, i used the bio method for it and i couldnt use the existing functions ,
i used the ProfileForm .




# Mordad 11th 
i started the day fresh . Lets go!

**making the follow button avalable in the index page**







# BIG VOW
form now , whenever i want to use only a tags whenever i want to post something only with a button! becouse its a hard to style a button and i want ot use a tag to head to a func

i added the follow button to the index page and its working fine with help pf ai actually to provide me a nice CBV 
the thing is that i cant style its buttom



# Mordad 11th 11 am
**Heading to post create form**

```python
class PostCreateForm(forms.ModelForm):
    category= forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ['title', 'post_author', 'category', 'content', 'image_file', 'audio_file']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
```
this code is so instructive, i learnde how to have a manytomany fiekd in a form


**i should add another condiotion to popular posts rather than the coundted views**
i should add the date for at most 3 days