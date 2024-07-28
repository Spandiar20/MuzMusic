from django.urls import path
from .views import BlogView,BlogSingleView

app_name='blog'

urlpatterns = [
    path('',BlogView.as_view(),name='blog_view'),
    path('single-view/<int:pk>',BlogSingleView.as_view(), name='single_view')
]
