from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from bot import bot, my_chat_id
from datetime import datetime

# Create your views here.
data = {
    'phone': '+998 99 428 77 96',
    'email': 'n.soatov@bk.ru',
    'address': 'Tashkent',
}


def home(request):
    context = {

    }
    return render(request, 'index.html', context=context)


def works(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
        'text': ProjectsDecription.objects.get(id=1)
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
            bot.send_message(my_chat_id, f'''
New callback from: <b>{form.cleaned_data['name']}</b>

Email: {form.cleaned_data['email']}

Topic: {form.cleaned_data['topic']}

Text: {form.cleaned_data['text']}

Time: {datetime.today().strftime('%D %H:%M:%S')}''', parse_mode='HTML')
            return redirect('home')
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'contact.html', context=context)

