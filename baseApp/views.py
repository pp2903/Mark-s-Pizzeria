from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request, "baseApp/index.html")


def about(request):    
    return render(request,'baseApp/about.html')



def menu(request):

    return render(request, 'baseApp/order.html')



def signUp(request):
    context = {}
    form = UserRegistrationForm
    context["form"] = form
    if(request.method=="POST"):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
    
    return render(request,'baseApp/signUp.html',context = context)



def login(request):
    context=  {}
    # form = 
    return render(request,'baseApp/login.html')

@login_required
def checkout(request):

    return render(request, "baseApp/checkout.html")

    