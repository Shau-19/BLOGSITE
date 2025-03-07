from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .models import Article
from .forms import ArticleForm
def aboutUS(request):
    return render(request,"about.html",)
    

def home(request):
    d={
        'title': 'Home page',
        'g':'Welcome to Your Story',
        'list': ["Blogs",'Articles','Stories'],
        'name':'By Shaurya Jain'

    }
    #return render(request,"index.html")
    return render(request,"abcd.html",d)


def article(request):
    return render(request,"article.html")

def efg(request,No):
    return HttpResponse(No)

def story(request):
    return render(request,"story.html")

def storymenu(request):
    return render(request,'storymenu.html')


def share(request):
    return render(request,"share.html")

def upload_blog(request):
    return render(request,"uploadB.html")

def upload_story(request):
    return render(request,"uploadS.html")

'''def upload_article(request):
    return render(request,"uploadA.html")'''





def upload_article(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()  # Ensuring title is retrieved
        content = request.POST.get('content', '').strip()
        file = request.FILES.get('file', None)

        # Validate that title is not empty
        if not title:
            return render(request, 'uploadA.html', {'error': "Title cannot be empty"})

        # Save to database
        Article.objects.create(title=title, content=content, file=file)
        
        return redirect('article_list')  # Redirect to the articles list

    return render(request, 'uploadA.html')





