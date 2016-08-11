#coding: utf-8
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post,Comment


# Create your views here. 
def index(request):
    posts = Post.objects.all().order_by('-published_date')
    user = request.user 
    context = {'posts' : posts,'current_user':user,} #request한 사람이 누구인지를 변수로 만들어 던져줌
    return render(request, 'blog/index.html', context)

def write(request): ## request is one of the django's own objects
    post = Post() ## creating new object for our model
    post.author = request.user ## store author in post.author from request.user, django will make request for our model
    post.title = request.POST['title']
    post.text = request.POST['text']
    post.published_date = timezone.now()
    post.save()

    return redirect('blog.views.index')
    
def delete(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.delete()
    return redirect('blog.views.index')
    
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST": ## get dictionary, get is used transferring pk
        post.author = request.user
        post.title = request.POST['title']
        post.text = request.POST['content']
        post.published_date = timezone.now()
        post.save()
        return redirect('blog.views.index')
    else:
        context={'post' : post}
        return render(request, 'blog/post_edit.html', context)

def reply_write(request):
    comment = Comment()
    # Comment는 비록 post라는 attribute를 가지지만 Post 모델의 인스턴스와 1:N의 관계를
    # 맺으려면 _id를 덧붙여서 post_id 즉 primary key를 통해 관계를 맺을 수 있다.
    comment.post_id = request.POST['id_of_post'] #post의 pk를 다루기 위함! id_of_post > name!
    comment.author = request.user
    comment.text = request.POST['content']
    comment.save()
    
    return redirect('blog.views.index')
    
def reply_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk) #get방식은 인자를 알려줌
    comment.delete()
    
    return redirect('blog.views.index')