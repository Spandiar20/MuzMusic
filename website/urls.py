from django.urls import path
from django.views.generic import TemplateView

app_name='website'

urlpatterns = [
    path('', TemplateView.as_view(template_name="website/index.html"),name='index'),
    path('about', TemplateView.as_view(template_name="website/about.html"),name='about'),
    path('contact', TemplateView.as_view(template_name="website/contact.html"),name='contact'),



]