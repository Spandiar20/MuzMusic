from django import forms
from .models import Post,Category


choices = Category.objects.all().values_list('title','title')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','post_author','category','content','image_file','audio_file']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'post_author':forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),

        }

 
class PostEditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','post_author','category','content','image_file','audio_file']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),

        }
 
