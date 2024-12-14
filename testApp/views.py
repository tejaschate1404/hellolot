from django.shortcuts import render, redirect
from .models import Category
from .models import ITService


def testCode(request):
    return render(request, 'home.html')


def services(request):
    return render(request , 'newservices.html')




def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Category.objects.create(name=name, description=description)
            return redirect('add_category')
    categories = Category.objects.all()
    return render(request, 'add_category.html', {'categories': categories})



def add_service(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        
        if title and category_id:
            category = Category.objects.get(id=category_id)
            ITService.objects.create(title=title, category=category, description=description)
            return redirect('view_services')

    return render(request, 'add_service.html', {'categories': categories})


def view_services(request):
    services = ITService.objects.select_related('category').all()
    return render(request, 'view_services.html', {'services': services})
