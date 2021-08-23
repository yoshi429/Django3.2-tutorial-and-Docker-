from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm
# Create your views here.

def article_detail_view(request, id=None, *args, **kwargs):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)

    context = {
        "article": article
    }

    return render(request, "articles/detail.html", context=context)


def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("search")
    article = None
    
    try:
        query = int(query)
    except:
        query = None

    if query is not None:
        article = Article.objects.get(id=query)
    context = {
        "article": article
    }  
    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request): 
    
    form = ArticleForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        title = request.POST['title']
        content = request.POST['content']
        obj = Article.objects.create(title=title, content=content)
        context['object'] = obj
        context['created'] = True

    return render(request, "articles/create.html", context=context)