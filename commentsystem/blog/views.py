from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  #csrf_exempt 를 사용하기 위함
from django.http import HttpResponse
import json
# from django.core import serializers  #json 방식으로 리턴 해주기 위해

# Create your views here.
def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {
        'posts': posts,
        }
    )

def new(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return render(request, 'index.html', {
                'posts': posts,
                }
            )
    else:
        form = PostForm()
    return render(request, 'new.html', {
        'form': form,
        }
    )

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all

    form = CommentForm()

    return render(request, 'detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        }
    )

@csrf_exempt
def  add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        if request.is_ajax():
            form = CommentForm(request.POST or None)
            data = request.POST.get("commentBody")
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()

                # return HttpResponse(dump, content_type='application/json')
                # return HttpResponse(simplejson.dumps(response_dict),
                            # mimetype='application/json')
                # ajax가 아닐 때
                # return redirect('detail', post.id)
                return JsonResponse(comment.body, safe=False)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {
        'post': post,
        'form': form,
        }
    )

