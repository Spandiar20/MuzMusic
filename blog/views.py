from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.db.models import Q,F
from account.models import Profile
from django.shortcuts import get_object_or_404

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
    paginate_by = 3  # Default pagination
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
            queryset = queryset.filter(category__title=cat_name)
        
        # Filter by author if provided
        author_name = self.kwargs.get('author_name')
        if author_name:
            queryset = queryset.filter(author__username=author_name)
        return queryset





class BlogCategoryView(BasePostListView):
    template_name = 'blog/blog-home.html'
    
    def get_queryset(self):
        return super().get_queryset()  # Calls the base logic to filter by category


class BlogAuthorView(BasePostListView):
    template_name = 'blog/blog-home.html'
    
    def get_queryset(self):
        return super().get_queryset()  # Calls the base logic to filter by author


class BlogHomeView(BasePostListView):
    template_name = 'blog/blog-home.html'  # Specify the template for the main blog view






class BlogSingleView(DetailView):
    model=Post 
    template_name='blog/blog-single.html'
    context_object_name='post'   


    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        Post.objects.filter(id=self.kwargs.get('pk')).update(counted_views=F('counted_views') + 1)
        # if you use get instead of filter you are encountring an error! = > AttributeError at /blog/single-view/1
        # 'Post' object has no attribute 'update'

        # this was a solution!
        # post=Post.objects.get(id=self.kwargs.get('pk'))
        # post.counted_views +=1
        # post.save()
        return context  