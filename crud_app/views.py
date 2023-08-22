from django.shortcuts import render

# Post 모델을 import
from .models import Post

# Create your views here.

# Read관련 함수 
def index(request): # 전체 게시물 출력
    posts = Post.objects.all()
    
    context = {
        'posts' : posts,
    }
    
    return render(request, 'index.html', context)

def detail(request, id):    # 하나의 게시물 출력
    post = Post.objects.get(id=id)
    
    context = {
        'post' : post
    }
    
    return render (request, 'detail.html', context)