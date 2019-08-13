from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UploadForm
from .models import Upload
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        

        if user is not None:
            auth.login(request, user)
            if user.groups.filter(name='Recipient'):
                return redirect('index')
            else:
                return redirect('uploader')

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

@login_required(login_url='/')
def index(request):
    return render(request,'index.html')

def is_member(user):
    return user.groups.filter(name='Uploader').exists()

@login_required(login_url='/')
@user_passes_test(is_member)
def uploader(request):
    return render(request,'uploader.html')

@login_required(login_url='/')
@user_passes_test(is_member)
def upload(request):         
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_item = form.save(commit=False)
            upload_item.uploaded_by = request.user
            upload_item.save()
            send_mail(upload_item.title, upload_item.description,settings.EMAIL_HOST_USER,[upload_item.send_to])
            return redirect('success')
        else:
            return HttpResponse("Not Valid")
    else:
        form = UploadForm()
        return render(request,'upload.html', {'form' : form})

@login_required(login_url='/')
def receive(request):     
    uploads = Upload.objects.filter(send_to=request.user.email)
    
    return render(request,'receive.html',{'uploads':uploads})

@login_required(login_url='/')
def success(request):
    return render(request,'success.html')

@login_required(login_url='/')
def upload_history(request):
    uploads = Upload.objects.filter(uploaded_by=request.user)

    return render(request,'upload_history.html',{'uploads':uploads})

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def error_404(request, exception):
    return render(request,'404.html')

def error_500(request):
    return render(request,'500.html')