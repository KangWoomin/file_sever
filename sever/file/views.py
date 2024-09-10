from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
# Create your views here.

def main(request):
    return HttpResponse('안녕')

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