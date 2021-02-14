from django.shortcuts import render

# Create your views here.
from blog.models import Post # imports models
    
def get_context_data(request): #send template info from DB
    context = dict()
    context["posts"] = Post.objects.all()
    # recent_post = Post.objects.get(id__exact=1)
    return render(request, 'index.html', context)