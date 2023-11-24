from django.shortcuts import render

# Create your views here.

def staticfolder(request):
    return render(request,'staticfolder.html')