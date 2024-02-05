from django.shortcuts import render, redirect, Http404, reverse
from django.http import HttpResponseNotFound, HttpResponse
from .forms import CreateUserForm, LoginForms
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


username = ''


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'registerform': form}
    return render(request, 'register.html', context=context)


def login_user(request):
    global username
    titles = 'Login page'
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')

    context = {'loginform': form,
               'titles': titles}

    return render(request, 'login.html', context)


def logout_user(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    yData = [22, 13, 14, 15, 16, 17, 18, 20, 22, 18, 13, 16, 14, 23, 22, 21, 23, 18]
    xData = ['12-00', '12-10', '12-20', '12-30', '12-40', '12-50', '13-00', '13-10', '13-20', '13-30', '13-40', '13-50',
             '14-00', '14-10', '14-20', '14-30', '14-40', '14-50']
    data = {'12-00': 22, '12-10': 13, '12-20': 14, '12-30': 15, '12-40': 16, '12-50': 17, '13-00': 18, '13-10': 20,
            '13-20': 22, '13-30': 18, '13-40': 13, '13-50': 16, '14-00': 14, '14-10': 23, '14-20': 22, '14-30': 21,
            '14-40': 23, '14-50': 18}
    context = {'username': username,
               'titles': 'Главная страница',
               'ydata': yData,
               'xdata': xData,
               'data': data}
    print(len(data))
    return render(request, 'index.html', context=context)




@login_required(login_url='login')
def about(request):
    context = {'username': username,
               'titles': 'About page', }
    return render(request, 'about.html', context=context)


def post_db(request, cat_slug):
    if cat_slug == 'post':
        print(request.GET)
        return HttpResponse(f'<p>iis</p>sss</p>')
    # http://127.0.0.1:8000/post_db/post/?code=ts&type=gs&date={sl,15.5,20}
    else:
        raise Http404()

    # return render(request, 'post_db.html')


@login_required(login_url='login')
def room(request, room_id):
    if request.method == 'GET':
        date_list = [
            {'id': 1, 'num': 12, 'title': 'Заголовок1'},
            {'id': 2, 'num': 13, 'title': 'Заголовок2'},
        ]
        keys = [key for key in date_list[0].keys()]
        context = {'room_name': room,
                   'titles': 'Залл',
                   'username': username,
                   'date_list': date_list,
                   'keys': keys}
        template = f'room{room_id}.html'
        return render(request, template_name=template, context=context)
    else:
        return render(request, 'rooms.html')


@login_required(login_url='login')
def archive(request, year):
    if year < 2024:
        raise Http404

    context = {'year': year,
               'titles': 'Архив',
               'username': username}
    return render(request, 'archive.html', context=context)


def not_found(request, exception):
    return HttpResponseNotFound('<p>Page not found</p>')

