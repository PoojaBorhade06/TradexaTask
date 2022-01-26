from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from.forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def testView(request):
    template_name='UserApp/base.html'
    context={}
    return render (request, template_name, context)

@login_required(login_url='login')
def addPostView(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showorder')
            #return HttpResponse('order Placed')
    template_name='ProductsApp/addorders.html'
    context={'form':form}
    return render (request,template_name,context)

def showPostView(request):
    template_name='ProductsApp/showorders.html'
    ords=Product.objects.all()
    context={'ords':ords}
    return render(request,template_name,context)
