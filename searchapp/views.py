# Import necessary modules

from django.shortcuts import render,get_object_or_404

from .models import  Book, Booktype

from django.db.models import Q

# Define function to display all books

def book_list(request):

    book = Book.objects.all()

    return render(request, 'book_list.html', {'book': book })


# Define function to display the particular book

def book_detail(request,id):

    book = get_object_or_404(Book, id=id)

    types = Booktype.objects.all()

    t = types.get(id=book.type.id)

    return render(request, 'book_detail.html', {'book': book, 'type': t.btype})


# Define function to search book

def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = Book.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(price__icontains=query) | Q(publication__icontains=query) )

    return render(request, 'search.html', {'query': query, 'results': results})
