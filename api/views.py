from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from api.models import Book


def index(request):
    return HttpResponse('SERVICES WILL BE UPDATE LATER...!!!')

#
# def index(request):
#     u = request.user.id
#     #owner_books = Book.objects.all()
#     owner_books = Book.objects.filter(owner=request.user.id)
#     return render(request,'index.html',context={'owner_books':owner_books,'u':u})

# def BookListView(generic.ListView):
#     model = Book
#     def get_queryset():
#         return Book.objects.all()
