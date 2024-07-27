# 6 Mordad 2:30 pm
**The first steps of the project:**

- Initializing the project,making a venv and installing the needed packages
- Just started the three app => website,blig,account 
- lets go config the apps and implement their urls
- lets go do the templates and static files


**what is the difference between STATIC_ROOT AND STATICFIELS_DIR?**

In Django, STATICFILES_DIRS and STATIC_ROOT serve different purposes within the context of static file management:
STATICFILES_DIRS: This setting is a list of directories where Django's staticfiles app will look for static files (such as CSS, JavaScript, and image files) when collecting them for deployment. These directories should contain the static files used by your project's various apps. The default value for this setting is an empty list, but you can define multiple directories as needed.
In the example you provided:
```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```

Django will look for static files in both BASE_DIR / "static" (a path relative to your project's base directory) and /var/www/static/ (an absolute path) when collecting static files.
STATIC_ROOT: This setting defines the absolute filesystem path where Django's collectstatic command will collect all the static files from the locations defined in STATICFILES_DIRS. The collected files are placed in the directory specified by STATIC_ROOT, and this directory should be served by your web server during deployment.
Example:

```python
STATIC_ROOT = "/var/www/myproject/static/"
```

 **warning**
  (staticfiles.E002) The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.

This warning appears because the STATICFILES_DIRS setting should not include the directory specified in the STATIC_ROOT setting. The STATICFILES_DIRS setting is meant to specify the locations where Django should look for static files during development, while STATIC_ROOT is the destination directory where Django collects static files for deployment.
Including STATIC_ROOT in STATICFILES_DIRS can lead to issues during the static file collection process. When you run collectstatic, Django will try to copy the contents of STATIC_ROOT into itself, which might result in duplicated files, confusion during development, or errors during deployment.
To resolve this issue, make sure that STATICFILES_DIRS only contains the directories where your project's static files are located, excluding STATIC_ROOT. In your case, remove /var/www/static/ from STATICFILES_DIRS since it is already set as STATIC_ROOT.

**worth noting**
Its important to load the static in the base.html even if there are no directly static tags in it.


# Models
**Mordad 6th 4:00 pm**

**post validation**
i didin't want to force the user to have image and audio and content for his/her posts at the same time , so i needed a way to make sure that when saving a post , at ;east pne of these fields has value
- my solution
well maybe i can do the validation at the form created for posts but you know what i learning ! So lets just experiment ! Lets fo it in the post model:

```python 
    
    def clean(self):
        if (not self.image_file and not self.audio_file and not self.content):
            raise ValidationError("Either field1 or field2 must have a value.")

        super().clean()

```


**conmments for dead users**
so what should i do if a user deletes his/her account ? i will delete his posts, what about his comments? i want to let the comments stay

```python 
# in the comment model
comment_author = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
def __str__(self):
    try:
      return f'{self.commnet_author.username} : {self.content[:30]}'
    except:
      return f'no author : {self.content[:30]}'
    

```


**post relationship with authors and comments**
a simple foreingkey to the user table
- ManyToOne relationship is the same as foreignKey
So what to do for the comments?

DONT WE HAVE A OneToMany RELATIONSHIP?
Yes, Django and other relational databases also support "one-to-many" relationships. In a "one-to-many" relationship, a single object of one model can be related to multiple objects of another model. This is essentially the reverse of a "many-to-one" or "foreign key" relationship.
In Django, you can define a one-to-many relationship using a ForeignKey field on the "many" side, just like a many-to-one relationship. Django automatically creates a reverse relationship manager called <lowercase_model_name>_set on the "one" side, which allows accessing all related objects from the "many" side.




**user model**
i want a have a profile class which has a foreignkey to the django user table 
so I have to use signals

```python
#account.signals.py

from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,**kwargs): 
    if created:
        #Profile.objects.create(user=instance)
        user_profile=Profile(user=instance)
        user_profile.save()
        #Each user should follow him/herself
        user_profile.follow.set([instance.profile.id])
        user_profile.save()

#post_save.connect(post_save_create_profile,sender=User) => without the decorator        



#account.apps.py
   def ready(self):
        import account.signals
#account.init.py
default_app_config='account.apps.AccountConfig'
```

**lets do some magic in the admin panel of the account**
i learend how to unregsiter a model which is in the admin panel and how to mix to models into one , so that i can see them together in the admin panel
```python 

from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


admin.site.register(User,UserAdmin)
#mix profile info with user info
class ProfileInline(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    #just display username field on  admin page
    fields=['username']
    inlines=[ProfileInline]

#unregister the initial user
admin.site.unregister(User)

#register the new user panel
#admin.site.register(Profile)
#When wecreat the ProfileInline class  there is no need for the above line


```
**how to make the following option for users?**
```python

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    follow = models.ManyToManyField('self',related_name='follwed_by',
                                    symmetrical=False,blank=True)
 ```



# Mordad 6th 6:00 pm
now i dont really know what should the author field in the Post model , refer to!
User or Profile? Imma refer it the Profile

