from django.shortcuts import render
from . forms import SearchForm
from . models import Book
from django.db.models import Q

# Create your views here.
def search_view(request):
    form = SearchForm() 
    results = []

    """if request.GET.get('query'):
        query = request.GET['query']
        #results = Book.objects.filter(title__icontains=query)
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )"""
    
    if request.GET:
        query = request.GET.get('query')
        tags = request.GET.get('tags')
        q_objects = Q()

        if query:
            q_objects &= Q(title__icontains=query) | Q(author__icontains=query)

        if tags:
            tag_list = [tags.strip() for tag in tags.split(',')]
            for tag in tag_list:
                q_objects &= Q(tags__name__in=[tag])

        results = Book.objects.filter(q_objects).distinct()

    return render(request, 'search.html', {'form': form, 'results': results})