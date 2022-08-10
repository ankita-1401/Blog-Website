from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def PostList_view(request):
    post_list=Post.objects.all()
    return render(request,'blog/postlist.html',{'post_list':post_list})

def PostDetail_view(request,year,month,day,post):
    Post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/postdetail.html',{'post':Post})
