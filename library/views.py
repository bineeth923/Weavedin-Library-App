from django.shortcuts import render
from library import models
def index(request):
    all_books = models.Book.objects.all()
    all_author = models.Author.objects.all()
    context = {
        'books' : all_books,
        'authors' : all_author
    }
    if(request.POST):
        book = models.Book()
        book.name = request.POST['name']
        book.author = models.Author.objects.get(name=request.POST['author'])
        book.isbn = request.POST['isbn']
        book.description = request.POST['description']
        book.save()
    return render(request , 'library/index.html' , context=context)

def author(request):
    all_authors = models.Author.objects.all()

    if(request.POST):
        auther = models.Author()
        auther.name = request.POST['author']
        auther.country = request.POST['country']
        auther.age = request.POST['age']
        auther.gender = request.POST['gender']
        auther.description = request.POST['description']
        auther.save()
    context = {
        'authors' : all_authors,
    }
    return render(request  ,'library/author.html' , context=context)

def book(request , id):
    next_book = 0
    pre_book = 0
    book_single = models.Book.objects.get(id=id)

    try:
        models.Book.objects.get(id=int(id)+1)
        next_book = int(id)+1
    except:
            next_book = id

    try:
        models.Book.objects.get(id=int(id)-1)
        pre_book = int(id)-1
    except:
            pre_book = id
    context = {
        'book' : book_single,
        'pre_book' : pre_book,
        'next_book' : next_book
    }
    return render(request , 'library/book.html' , context=context)

def author_detail(request , id):
    books = models.Book.objects.all().filter(author=models.Author.objects.get(id=id))
    try:
        models.Book.objects.get(id=int(id)+1)
        next_book = int(id)+1
    except:
            next_book = id

    try:
        models.Book.objects.get(id=int(id)-1)
        pre_book = int(id)-1
    except:
            pre_book = id
    context = {
        'pre_auth' : pre_book,
        'next_auth' : next_book,
        'author': models.Author.objects.get(id=id),
        'books': books
    }

    return render(request , 'library/author_indi.html' , context)