from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.db.models import Q,F

class BlogView(ListView):
    model=Post
    template_name='blog/blog-home.html'
    context_object_name='posts'
    paginate_by = 1 # Pagination over-write


    def get_queryset(self):
        query=self.request.GET.get('search')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(post_author__username__icontains=query)
            )
        else:
            return Post.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        if query and not context['posts']:
            context['no_results_message'] = f"No results found for '{query}'."
        return context   



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