from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'newsite/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            text = form.cleaned_data['text']
            Comment.objects.create(post=post, author=author, text=text)
    else:
        form = CommentForm()

    return render(request, 'newsite/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            text = form.cleaned_data['text']
            Comment.objects.create(post=post, author=author, text=text)
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'newsite/comment_form.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Post.objects.create(title=title, content=content)
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'newsite/post_form.html', {'form': form})