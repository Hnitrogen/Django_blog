from django.shortcuts import render
from django.utils import timezone 
from .models import Post
from django.shortcuts import render , get_object_or_404 
# Create your views here.

def post_list(request):
    #给文章按生成时间排序
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts' : posts}) 
    # { } 里面是给templates用的   ‘name’ : 

def post_detail(request,pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})