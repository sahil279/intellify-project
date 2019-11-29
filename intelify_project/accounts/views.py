from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Congratulations, Your account has been created,your username is {username}')
            return redirect('login')
    else:
        form = SignUpForm()



    return render(request,'accounts/signup.html',{'form':form})





def profile(request):

 		return render(request,'accounts/profile.html')