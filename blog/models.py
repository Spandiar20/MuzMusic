from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(Category)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    image_file=models.ImageField(upload_to='post_image_files')
    audio_file = models.FileField(upload_to='post_audio_files',null=True,blank=True)
    counted_views = models.IntegerField(default=1)
    post_author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='post_likes',null=True,blank=True)

    def get_absolute_url(self):
       return reverse('blog:single_view',kwargs={'pk':self.id})

    # This is new!
    def clean(self):
        if (not self.image_file and not self.audio_file and not self.content):
            raise ValidationError("Either content or image of audio must have a value.")

        super().clean()

    
    def __str__(self):
        return str(self.id) +':'+ self.title 
    

class Comment(models.Model):
  comment_author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  post=models.ForeignKey(Post,on_delete=models.CASCADE)
  content = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    try:
      return f'{self.commnet_author.username} : {self.content[:40]}'
    except:
      return f'no author : {self.content[:30]}'
    
  
class Reply(models.Model):
  reply_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
  content = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    try:
      return f'{self.replier.username} : {self.content[:30]}'
    except:
      return f'no author : {self.content[:30]}'  
