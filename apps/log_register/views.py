from django.shortcuts import render, redirect, HttpResponse
from .models import User
from .forms import LoginForm, RegisterForm 
import bcrypt
from apps.master.views import *
from apps.tek_view.views import *
from apps.admin_view.views import *


def login(request):
    if 'id' in request.session:
        return redirect('/main')
    else:
        if request.method == 'GET':
            form = LoginForm()
        else:
            form = LoginForm(request.POST)
            if form.is_valid():
                user = User.objects.get(email=request.POST['email'])
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['is_admin'] = user.is_admin
                request.session['is_tech'] = user.is_tech
                if user.is_tech == True and user.is_admin == True:
                    return redirect('/choose_view')
                elif user.is_tech == True:
                    return redirect('/tek_view/tech_view')
                else:
                    return redirect('/admin_view/admin_view')
        return render(request, 'log_register/login-page.html', {'form': form})


def register(request):
    if 'id' in request.session:
        return redirect('/main_page')
    else:
        if request.method == 'GET':
            form = RegisterForm()
        else:
            form = RegisterForm(request.POST)
            if form.is_valid():
                mods = form.save(commit = False)
                hashed_pass = bcrypt.hashpw(
                    request.POST['password'].encode(), bcrypt.gensalt()).decode()
                mods.password = hashed_pass
                form.save()
                user = User.objects.get(email=request.POST['email'])
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['is_admin'] = user.is_admin
                request.session['is_tech'] = user.is_tech
                if user.is_tech == True and user.is_admin == True:
                    return redirect('/choose_view')
                elif user.is_tech == True:
                    return redirect('/tek_view/tech_view')
                else:
                    return redirect('/admin_view/admin_view')
        return render(request, 'log_register/register-page.html', {'form': form})


