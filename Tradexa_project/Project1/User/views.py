from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.
def loginView(request):
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        #return HttpResponse('Here write')
        user=authenticate(username=u,password=p)#.using('users')#1.user object=valid credentials
                                                 #2.None=Invalid Credentials
        if user is not None:
            print('Valid credentials')
            login(request,user)
            #return redirect('showorder')
            return HttpResponse('Login sucessfully')
        else:
            print('Invalid credentials')
            messages.error(request,'Invalid credentials')
    template_name='UserApp/login.html'
    context={}
    return render(request,template_name,context)

def registerView(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST) #.using('users')
        if form.is_valid():  #.using('users'):
            form.save()
            return redirect('login')
            #return HttpResponse('Account Created!!')
    template_name='UserApp/register.html'
    context={'form':form}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)#.using('users')
    return redirect('login')


