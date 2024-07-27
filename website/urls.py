from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="website/index.html")),
    path('about/', TemplateView.as_view(template_name="website/about.html"))

]