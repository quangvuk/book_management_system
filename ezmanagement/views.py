from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from api.models import  User, Book, Author
from .forms import UserForm



# Create your views here.

def process_request(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return render(request, 'admin/admin_book.html')
        else:
            return render(request, 'user/user_book.html')
    else:
        return HttpResponseRedirect('/ezmanagement/login/')


def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/ezmanagement/')
    usr = psw = ''
    if request.POST:
        usr = request.POST.get("username")
        psw = request.POST.get("password")

        user = authenticate(username=usr, password=psw)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/ezmanagement/')
    return render(request, 'registration/login.html')


def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/ezmanagement/login/')
    return render(request, 'registration/login.html')


def query_books(request):
    if request.user.is_superuser:
        books = Book.objects.all()
        return render(request, 'admin/admin_book.html', context={'books':books})
    else:
        books = Book.objects.filter(owner_id=request.user.id)
        return render(request, 'user/user_book.html', context={'books': books})



def query_users(request):
    users = User.objects.all()
    return render(request, 'admin/admin_user.html',context={'users':users})


def query_authors(request):
    authors = Author.objects.all()
    return render(request, 'admin/admin_author.html', context={'authors':authors})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

    else:
        form = UserForm()
    return render(request,'admin/_add_user.html',{'form':form})

