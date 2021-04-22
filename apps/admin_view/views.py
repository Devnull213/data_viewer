from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from apps.tek_view.models import *
from apps.tek_view.views import *

def admin_view(request):
	return render(request, 'admin_view/main.html')

def stulz_one_data(request):
	Stulz = Stulz_one.objects.get(id = 2)
	data = {
		'stulz_temp': Stulz.temperature,
		'stulz_hum': Stulz.humidity,
		'stulz_com': Stulz.comment,
	}
	return JsonResponse(data)
