from django import forms
from .models import Post,Category


choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','author','category','content','post_image','post_audio']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),

        }

 
class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','author','category','content','post_image','post_audio']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),

        }
 
