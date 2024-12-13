from django.shortcuts import render

def testCode(request):
    return render(request, 'home.html')
