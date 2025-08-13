from django.contrib import admin
from .models import Post, Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')
    inlines = [ComentarioInline]

admin.site.register(Post, PostAdmin)
