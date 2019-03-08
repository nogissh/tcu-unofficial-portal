from django.shortcuts import render
from .models import Post
from .forms import Contribution
from django.shortcuts import redirect
from django.contrib.auth.models import User
import datetime

# Create your views here.
def index(request):
    return render(request,'app/index.html')


def post(request):
    data = Post.objects.all()
    params = {
        "data":data,
        "form":Contribution(),
    }

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        date_update = datetime.datetime.now()
        term_start = request.POST['term_start']
        term_end = request.POST['term_end']

        user = User.objects.get(id=request.POST['user'])


        contribution = Post(title=title,text=text,date_update=date_update,term_start=term_start,term_end=term_end,user=user)#,date_post=date_postdate_update=date_update,
        contribution.save()
        return redirect(to='/app/home/')
    return render(request,'app/post.html',params)
