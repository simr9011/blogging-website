from django.shortcuts import render
from .models import Blogpost
from django.views.generic import View
from .forms import Addblog
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request,'app7/basic.html')
def blog(request):
    myposts=Blogpost.objects.all()
    return render(request,'app7/blogs.html',{'mypost':myposts})
def blogpost(request,id):
    p=Blogpost.objects.get(post_id=id)
    return render(request,'app7/Blogpost.html',{'post':p})
def home(request):
    return render(request,'app7/home.html')
class addblog(View):
    def get(self,request):
        form=Addblog(None)
        return render(request,'app7/addblog.html',{'f':form})
    def post(self,request):
        form=Addblog(request.POST,request.FILES)
        form.save()
        return redirect('/blog')
def search(request):
    query=request.GET.get('search')
    if query:
        match=Blogpost.objects.filter(title__startswith=query)
        return render(request,'app7/blogs.html',{'mypost':match})
