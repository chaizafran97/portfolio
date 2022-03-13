from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
    posts = Post.object.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories_name_contains=category).order_by(-'created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments":comments,
    }
    return render(request, "blog_detail.html", context)
