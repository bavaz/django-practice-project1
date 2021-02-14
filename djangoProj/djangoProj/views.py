from django.shortcuts import render # imports basic template view of Django
from django.views.generic.base import View
from django.views.generic import TemplateView
from blog.models import Post # imports models

class post_feed(TemplateView): # renders DB contents
    template_name = 'index.html'
    
def get_context_data(self, *args, **kwargs): #send template info from DB
    context = dict()
    context["posts"] = Post.objects.all()
    console.log(len(context))
    return context