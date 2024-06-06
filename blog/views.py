from django.shortcuts import render, redirect
from .models import Category, Post,Recommended_Posts,About
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def home(request):
    categories = Category.objects.all()
    about = About.objects.first()
    recommended = Recommended_Posts.objects.all().order_by('-created_at')[:5]
    posts = Post.objects.all().order_by('-created_at')
    page = request.GET.get('page',1)
    paginator = Paginator(posts,7)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    for post in posts:
        post.category = post.categories.all()

    return render(request, 'index.html', {'categories': categories,'posts':posts,'recommended':recommended,'about':about})


def article(request, title):
    categories = Category.objects.all()
    about = About.objects.first()
    recommended = Recommended_Posts.objects.all().order_by('-created_at')[:5]
    try:
        post = Post.objects.get(slug=title)
        post_categories = post.categories.all()  # Access categories associated with the post
    except Post.DoesNotExist:
        return redirect('/404')  # Redirect to appropriate URL
    return render(request, 'article.html', {'post': post, 'post_categories': post_categories,'categories': categories,'recommended':recommended,'about':about})

def about(request):
    categories = Category.objects.all()
    recommended = Recommended_Posts.objects.all().order_by('-created_at')[:5]
    about = About.objects.first()
    return render(request, 'about.html',{'about':about,'categories': categories,'recommended':recommended})
def article_cat(request,title):
    categories = Category.objects.all()
    recommended = Recommended_Posts.objects.all().order_by('-created_at')[:5]
    about = About.objects.first()
    try:
        cat = Category.objects.get(slug=title)
    except Category.DoesNotExist:
        return redirect('/404')

    posts = Post.objects.filter(categories = cat.id).order_by('-created_at')
    page = request.GET.get('page',1)
    paginator = Paginator(posts,10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    for post in posts:
        post.category = post.categories.all()
    return render(request,'article_cat.html',{'posts':posts,'about':about,'categories': categories,'recommended':recommended})
def search(request):
    categories = Category.objects.all()
    recommended = Recommended_Posts.objects.all().order_by('-created_at')[:5]
    about = About.objects.first()
    query = request.GET.get('query')
    if not query:
        return redirect('/')
    posts = Post.objects.filter(title__icontains = query).order_by('-created_at')
    page = request.GET.get('page',1)
    paginator = Paginator(posts,10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    for post in posts:
        post.category = post.categories.all()
    return render(request,'article_cat.html',{'posts':posts,'about':about,'categories': categories,'recommended':recommended})
def e404(request):
    return render(request,'404.html')
