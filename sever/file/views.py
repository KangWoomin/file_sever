from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from .forms import Video_form
from .models import Video


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
            return redirect('action')
        else:
            content = {
                'error':'로그인에 실패 하였습니다.'
            }
            return render(request,'login.html',content)
        
    return render(request ,'login.html' )

def user_logout(request):
    logout(request)
    return redirect('main')

from django.contrib.auth.decorators import login_required

@login_required
def action(request):
    return render(request, 'action.html')


def upload_video(request):
    if request.method =='POST':
        form = Video_form(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('action')
    else:
        form = Video_form()
    return render(request,'upload_video.html',{'form':form})



from django.http import JsonResponse
def upload_video_api(request):
    if request.method == 'POST':
        video_file = request.FILES.get('video_file')

        if video_file:
            video = Video(video_file=video_file)
            video.save()
            return JsonResponse({'message': "저장 완료"}, status = 201)
        return JsonResponse({'message':'error'}, status = 400)
    
    return JsonResponse({'error':'POST로 전달 해야합니다.'}, status = 405)



import cv2
import numpy as np
import requests
from datetime import datetime
def receive_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        condition = request.POST.get('condition')
        if video_url:
            process_stream(video_url, condition)
            return JsonResponse({'message':'스타트'}, status=200)
        return JsonResponse({'message':'error'}, status=400)
    return JsonResponse({'message':'POST로 접근 가능 합니다'}, status=405)



def process_stream(video_url, condition):
    cap = cv2.VideoCapture(video_url)
    if not cap.isOpened():
        print('Error')
        return 
    
    start_time = None
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if condition_met(frame, condition):
            if start_time is None:
                start_time = datetime.now()
            
            frames.append(frame)
        
        if start_time and (datetime.now() - start_time).second > 26:
            save_video(frames, 'output.mp4')
            frames = []
            start_time = None
    
    cap.release()

def condition_met(frame, condition):
    
     # 여기서 조건을 정의합니다 (예: 특정 객체 탐지, 움직임, 색상 등)
    # True를 반환하면 조건이 만족된 것
    return True


import os
from django.core.files.base import ContentFile
def save_video(frames):
    filname = datetime.now().strftime("%Y%m%d_%H%M%S")+'.mp4'
    height, width,_ = frames[0].shape
    out = cv2.VideoWriter(cv2.VideoWriter_fourcc(*'mp4v'),30,(width, height))

    for frame in frames:
        out.write(frame)
    out.release()

    file_path = os.path.join('videos/', filname)
    video = Video(upload_at = datetime.now())
    with open(filname, 'rb') as f:
        video.video_file.save(file_path, ContentFile(f.read()))
    video.save()


def video_list(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request,'video_list.html',{'videos':videos})