from django.shortcuts import render, redirect, HttpResponse
from apps.log_register import *

def index(request):
	return render(request, 'layout.html')

def main(request):
	return render(request, 'admin_view/main.html')

def choose_view(request):
    return render(request, 'choose_view.html')

def logout(request):
    request.session.clear()
    return redirect('/log_register/login')