from django.shortcuts import render, redirect

# Post 모델을 import
from .models import Post

# Create your views here.

# Read 관련 함수 
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

# create 관련 함수
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    post = Post()
    post.title = title
    post.content = content
    post.save()
    
    return redirect(f'/posts/{post.id}/')