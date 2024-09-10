from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
# Create your views here.

def main(request):
    return render(request,'base.html')

from .forms import UserModelForm
def create_user(request):
    if request.method =='POST':
        form = UserModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('main')
        
    else:
        form = UserModelForm()

    return render(request,'create_user.html',{'form':form})

from django.contrib.auth import authenticate
def user_login(request):
    if request.method == 'POST':
        userID = request.POST.get('userID')
        password = request.POST.get('password')

        user = authenticate(request, username = userID , password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request,'login.html',{'error':'접근 불가'})
    
        
    return render(request ,'login.html' )

def user_logout(request):
    logout(request)
    return redirect('main')