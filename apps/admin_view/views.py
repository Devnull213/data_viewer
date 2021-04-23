from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from apps.tek_view.models import *
from apps.tek_view.views import *

def admin_view(request):
	return render(request, 'admin_view/main.html')

def date_config(request):
	global the_date
	the_date = request.POST['date']
	return redirect('/admin_view/admin_view')

def stulz_one_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	stulz_date = Stulz_one.objects.all().filter(created_at__date=(the_date))
	temp = []
	hum = []
	for temper in stulz_date:
		temp.append(temper.temperature)
	for humi in stulz_date:
		hum.append(humi.humidity)
	data = {
		'temp': temp,
		'hum': hum,
		'labels': labels,
	}
	return JsonResponse(data)

def stulz_two_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	stulz_date = Stulz_two.objects.all().filter(created_at__date=(the_date))
	temp = []
	hum = []
	for temper in stulz_date:
		temp.append(temper.temperature)
	for humi in stulz_date:
		hum.append(humi.humidity)
	data = {
		'temp': temp,
		'hum': hum,
		'labels': labels,
	}
	return JsonResponse(data)