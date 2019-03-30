from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

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

def  add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post.id)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {
        'post': post,
        'form': form,
        }
    )

