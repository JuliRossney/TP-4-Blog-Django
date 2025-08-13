from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import ComentarioForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.save()
            return redirect('detalle_post', post_id=post.id)
    else:
        form = ComentarioForm()
    return render(request, 'blog/detalle_post.html', {'post': post, 'form': form})
