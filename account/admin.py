from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User



#admin.site.register(Profile)




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
admin.site.register(User,UserAdmin)
#When wecreat the ProfileInline class  there is no need for the above line


