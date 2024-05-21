from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

from .models import Signup

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'blog_page_members_app/index.html', context)

def about(request):
    return render(request, 'blog_page_members_app/about.html', {})

def article(request):
    return render(request, 'blog_page_members_app/article.html', {})

def blog(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.all().order_by('-timestamp')[0:3]
    articles = Article.objects.order_by('-created_at')
    context = {
        'object_list': featured,
        'latest': latest
    }


    return render(request, 'blog_page_members_app/blog.html', context )

def contact(request):
    if request.method == "POST":
        email_ = request.POST['email']
        number_ = request.POST['number']
        emri_ = request.POST['emri']
        yourmessage_ = request.POST['yourmessage']
        Signup(email = email_, number = number_, emri = emri_, yourmessage = yourmessage_).save()

    
    return render(request, 'blog_page_members_app/contact.html', {})

@login_required(login_url='/login/')
def editorpage(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            excerpt = form.cleaned_data['excerpt']
            thumbnail = form.cleaned_data['thumbnail']
            featured = form.cleaned_data['featured']
            author = Author.objects.get(user=request.user)
            article = Post(title=title, excerpt=excerpt, thumbnail=thumbnail, featured=featured, author=author)
            article.save()
            return redirect('/', pk=article.pk)
    else:
        form = ArticleForm()    
    return render(request, 'blog_page_members_app/editorpage.html', {'form':form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
    
        if user is not None:
            auth.login(request, user)
            return redirect('/')    
        else:
            return redirect('../blog')
    
    else:
        return render(request, 'blog_page_members_app/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if username=="" and password=="" and confirm_password=="":
            return redirect('../register/')
        else:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    return redirect('/')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.set_password(password)
                    user.save()
                    Author.objects.create(user=user)
                    return redirect('../login/')
    return render(request, 'blog_page_members_app/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def accessLogin(request):
    return render(request, "editorpage.html")