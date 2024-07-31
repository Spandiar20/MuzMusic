from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.db.models import Q,F
from account.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# class BlogView(ListView):
#     model=Post
#     template_name='blog/blog-home.html'
#     context_object_name='posts'
#     paginate_by = 1 # Pagination over-write


#     def get_queryset(self):
#         query=self.request.GET.get('search')
#         if query:
#             return Post.objects.filter(
#                 Q(title__icontains=query) |
#                 Q(content__icontains=query) |
#                 Q(post_author__username__icontains=query)
#             )
#         else:
#             return Post.objects.all()
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         query = self.request.GET.get('search')
#         if query and not context['posts']:
#             context['no_results_message'] = f"No results found for '{query}'."
#         return context   


class BasePostListView(ListView):
    model = Post
    paginate_by = 1  # Default pagination
    context_object_name='posts'

    def get_queryset(self):
        queryset = super().get_queryset()  # Retrieve all posts by default
        
        # Get the search query from GET parameters
        search_query = self.request.GET.get('search', '')
        if search_query:
            # Filter posts based on title, content, or author's username
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(post_author__username__icontains=search_query)
            )
        

           # Filter by category if provided
        cat_name = self.kwargs.get('cat_name')
        if cat_name:
            queryset = queryset.filter(category__slug=cat_name)
        # Filter by author if provided
        author_name = self.kwargs.get('author_name')
        if author_name:
            queryset = queryset.filter(post_author__username=author_name)
        return queryset
  




class BlogCategoryView(BasePostListView):
    template_name = 'blog/blog-home.html'
    
    def get_queryset(self):
        return super().get_queryset()  # Calls the base logic to filter by category

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class BlogAuthorView(BasePostListView):
    template_name = 'blog/blog-author.html'
    
    def get_queryset(self):
        return super().get_queryset()  # Calls the base logic to filter by author
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
    
        context['username']=self.kwargs['author_name']
        return context



class BlogHomeView(BasePostListView):
    template_name = 'blog/blog-home.html'  # Specify the template for the main blog view






class BlogSingleView(DetailView):
    model=Post 
    template_name='blog/blog-single.html'
    context_object_name='post'   


    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        Post.objects.filter(id=self.kwargs.get('pk')).update(counted_views=F('counted_views') + 1)
        post_tobe_liked=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=post_tobe_liked.total_likes()
        liked=False
        if post_tobe_liked.likes.filter(id=self.request.user.id).exists():
            liked=True
        context['liked']=liked
        context['total_likes']=total_likes    
        # if you use get instead of filter you are encountring an error! = > AttributeError at /blog/single-view/1
        # 'Post' object has no attribute 'update'

        # this was a solution!
        # post=Post.objects.get(id=self.kwargs.get('pk'))
        # post.counted_views +=1
        # post.save()
        return context  
    


# i dont like this func, i am feeling some code smell
# follwing and unfollowing
# i was a method in the account app, i didint even change the name so that i know there is code smell
# @login_required(login_url='account/login')
# def members_profile(request):
#         if request.method == 'POST':
#             current_user_profile=request.user.profile
#             action=request.POST['follow']
#             target_profile=request.POST['target_profile']
#             print(action)
#             if action == 'unfollow':
#                 current_user_profile.follows.remove(target_profile)
#             else:
#                 current_user_profile.follows.add(target_profile
#             current_user_profile.save()    
#             return HttpResponseRedirect(reverse('blog:blog_author',kwargs={'author_name':s}))        


@login_required
def likeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked =False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('blog:single_view',kwargs={'pk':pk}))        

