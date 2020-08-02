from django.shortcuts import render, redirect
from .forms import FileForm
from .models import UploadFile
from subprocess import *
from .media.callthisone import *

# def index(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             form.save()
#             return redirect('upload')
#     else:
#         form = FileForm()
#     return render(request, 'upfile/index.html', {'form': form})


def index(request):
    if request.method == 'POST':
        form = FileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = FileForm()
    return render(request, 'upfile/index.html', {'form': form})

def upload(request):
    load_files = UploadFile.objects.all()
    return render(request, 'upfile/upload.html', {'load_files': load_files})

def show(request):
    path = request.POST.get('file_btn', 'default')
    print(path)
    callthisfunc(request)
    #call(["python", path])
    #call('python upfile/media/callthisone.py')
    return render(request, 'upfile/show.html')
