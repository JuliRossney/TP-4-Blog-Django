from django.shortcuts import render, redirect
from .models import Post, Comentario
from .forms import ComentarioForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post_id = request.POST.get("post_id")  # a qué post pertenece
            comentario.usuario = request.user
            comentario.save()
            return redirect('lista_posts')
    else:
        form = ComentarioForm()

    return render(request, 'blog/lista_posts.html', {'posts': posts, 'form': form})
