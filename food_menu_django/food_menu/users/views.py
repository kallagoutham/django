from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #inbuilt to handle all the form serving techniques.
        if form.is_valid():
            #registers the user.
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account has been successfully created...!!!!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')