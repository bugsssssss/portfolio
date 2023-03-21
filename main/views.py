from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.urls import reverse_lazy



# Create your views here.
data = {
    'phone': '+998 99 428 77 96',
    'email': 'n.soatov@bk.ru',
    'address': 'Tashkent'
}


def home(request):
    context = {

    }
    return render(request, 'index.html', context=context)


def works(request):
    projects = Projects.objects.all()
    print(projects)
    context = {
        'projects': projects
    }
    return render(request, 'works.html', context=context)


def work_detail(request, pk):
    work = Projects.objects.get(id=pk)
    context = {
        'work': work,
        'all_works': Projects.objects.all()
    }
    return render(request, 'work.html', context=context)


def about(request):
    context = {
        'about': About.objects.get(id=1)
    }
    return render(request, 'about.html', context=context)


def contact(request):
    form = CallbackForm()
    if request.POST:
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'contact.html', context=context)
