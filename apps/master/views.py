from django.shortcuts import render, redirect, HttpResponse
from datetime import date
from apps.log_register.views import *
from apps.log_register.models import User
from apps.log_register.forms import EditProfileForm, EditPasswordForm

def index(request):
	return redirect('/log_register/login')


def main(request):
    return render(request, 'admin_view/main.html')


def choose_view(request):
    return render(request, 'choose_view.html')


def profile(request):
    user = User.objects.get(id=request.session['id'])
    if request.method == 'GET':
        form = EditProfileForm(instance=user)
        passform = EditPasswordForm(instance=user)
    else:
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.session['id'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return redirect('/profile')
    return render(request, 'perfil.html', {'form':form, 'user': user, 'passform': passform })



def logout(request):
    request.session.clear()
    return redirect('/log_register/login')