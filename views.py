from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from books.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from tagging.models import Tag
from tagging.utils import LOGARITHMIC

def index(request):
    query = request.GET.get("q")
    books = Book.objects.all()
    if query:
        books = books.filter(Q(name__contains=query) | Q(author__name__contains=query))
        
    paginator = Paginator(books, 16) # Show 5 events per page  
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        books = paginator.page(page)
    except (EmptyPage, InvalidPage):
        books = paginator.page(paginator.num_pages)
        
    popular_tags = Tag.objects.cloud_for_model(Book, steps=4, distribution=LOGARITHMIC, min_count=1)
    
    return render_to_response("index.html", {"books": books, 'popular_tags':popular_tags, "query":query }, context_instance=RequestContext(request))
    
def about(request):
    return render_to_response("about.html", context_instance=RequestContext(request))
    
def jci(request):
    return render_to_response("jci.html", context_instance=RequestContext(request))

def project(request):
    return render_to_response("project.html", context_instance=RequestContext(request))

def contact_thanks(request):
    return render_to_response("contact_thanks.html", context_instance=RequestContext(request))