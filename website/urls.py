from django.urls import path
from django.views.generic import TemplateView
from .views import IndexView


app_name='website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', TemplateView.as_view(template_name="website/about.html"),name='about'),
    path('contact', TemplateView.as_view(template_name="website/contact.html"),name='contact'),



]