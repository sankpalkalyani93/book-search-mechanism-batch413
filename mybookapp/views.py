from django.shortcuts import render
from . forms import SearchForm
from . models import Book
from django.db.models import Q

# Create your views here.
def search_view(request):
    form = SearchForm() 
    results = []

    if request.GET.get('query'):
        query = request.GET['query']
        #results = Book.objects.filter(title__icontains=query)
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    return render(request, 'search.html', {'form': form, 'results': results})