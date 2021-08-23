"""
To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article


def home(request):
    """
    Take in request(Django sends request)
    Return HTML as a response (We pick to return the response)
    """

    obj = Article.objects.get(id=1)
    
    context = {
        "title": obj.title, 
        "id": obj.id,
        "content": obj.content
    }
    
    # Django Templates
    HTML_STRING="""
    <h1>{title} (id: {id})</h1>
    <p>{content}</p>
    """.format(**context)

    return HttpResponse(HTML_STRING)