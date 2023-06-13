from django.shortcuts import render

# Create your views here.

def mdbbootstrap(request):
    return render(request,'md_bootstrap5.html')