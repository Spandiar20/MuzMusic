from django import template
from blog.models import Category,Post
from django.db.models import Count



register= template.Library()

@register.inclusion_tag('blog/post-category.html')
def post_category():
    category_counts=Category.objects.annotate(post_count=Count('post'))
    print(category_counts)
    cat_dict={}
    for category in category_counts:
        category_title=category.title
        category_count=category.post_count
        cat_dict[category_title]=category_count
        #annotate return a queryset which has the instances of the table and 
        # the added fields which were cpmputed form the existing fields
    return {
        'categories':cat_dict,
         }





@register.inclusion_tag('blog/popular-posts.html')
def popular_posts():
  posts = Post.objects.order_by('-counted_views')[:4]
  return {
    'posts':posts
  }


