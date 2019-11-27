from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import ContactForm,LoginForm

def home_page(request):
    return render(request,"home_page.html")  

def about_page(request):
    return render(request,"about_page.html")  

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    username = form['Username']
    password = form['Password']
    user = authenticate(request,username=username,password=password)
    
    if user is not None:
        print(request.user.is_authenticated())
        login(request,user)
        context['form'] = LoginForm()
        return redirect('/about')

    else:
        print('error')    
    return render(request,'auth/login_page.html',context)

def register_page(request):
    return render(request,'')

def contact_page(request):
    contact_form = ContactForm()
    context = {
        'form': contact_form
    }
    if request.method == "POST":
        print(request.POST)
    return render(request,"contact_page.html",context)          