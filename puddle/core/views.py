from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from item.models import Category,Item
from .forms import SignupForm
from django.contrib.auth import logout


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

#for contact page
def contact(request):
    return render(request, 'core/contact.html')

 #create user, if user=valid => saved in db
def signup(request):
    if request.method == 'POST':
       form = SignupForm(request.POST)

       if form.is_valid():
           form.save()
           return redirect('/login/')
    else:
        form = SignupForm()
    

    return render(request, 'core/signup.html', {
        'form': form
    })

#logout user, if logout button is pressed 
@login_required
def lgout(request):

    logout(request)
    return redirect('/')
