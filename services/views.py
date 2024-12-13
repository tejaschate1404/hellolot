from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request,"services2.html")

def details_Web_Development(request):
    return render(request,"Web_Development.html")

