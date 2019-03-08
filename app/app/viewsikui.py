from django.shortcuts import render
from .models import Post
from .forms import Contribution
from django.shortcuts import redirect
from django.contrib.auth.models import User
import datetime
from .usage import regist_post


def post_home(request):
    """
    投稿ページを表示
    """
    data = Post.objects.all()

    params = {
        "data":data,
        "form":Contribution(),
    }
    
    return render(request,'app/post_home.html',params)


def post_job(request):
    """
    投稿処理
    """
    status = regist_post(request, Post, User)

    contents = {
        'detail': 'Completed!!' if status else 'Failed.'
    }

    return render(request, 'app/post_job.html', contents)
