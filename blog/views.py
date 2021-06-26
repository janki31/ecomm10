from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def index(request):
    posts=Blogpost.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def blogpost(request,bid):
    post=Blogpost.objects.filter(post_id=bid)
    return render(request,'blog/blogpost.html',{'post':post[0]})
