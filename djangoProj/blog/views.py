from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from blog.models import Post # imports models

class post_feed(TemplateView): # renders DB contents
    template_name = 'index.html'
    
def get_context_data(request): #send template info from DB
    context = dict()
    context["posts"] = Post.objects.all()
    context['stringy'] = "stringy"
    # recent_post = Post.objects.get(id__exact=1)
    return render(request, 'index.html', context)