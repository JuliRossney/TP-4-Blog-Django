from django.shortcuts import render
from blog.models import Post

def home(request):
    ultimos_posts = Post.objects.all().order_by('-fecha_creacion')[:3]  # últimos 3 posts
    return render(request, 'portfolio/index.html', {'ultimos_posts': ultimos_posts})
