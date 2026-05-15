from django.shortcuts import render
from blog.data import posts

# Create your views here.

def blog(request):
    print('BLOG')
    
    context = {
        # 'text': 'Olá blog',
        'posts': posts
    }
    
    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):
    print('exemplo')
    
    context = {
        'text': 'Olá exemplo'
    }
    
    return render(
        request,
        'blog/exemplo.html',
        context,
    )