from django.shortcuts import render, redirect, HttpResponse
from .forms import * 
from apps.log_register.views import *

def tech_view(request):
	return render(request, 'tek_view/main.html' )



def data_center(request):
	return render(request, 'tek_view/data_center.html')


def azotea(request):
	chilleruniflairform = ChillerUniForm()
	return render(request, 'tek_view/azotea.html', {'chilleruniflairform': chilleruniflairform})


def sala_ups(request):
	stulzoneform = StulzOneForm()
	stulztwoform = StulzTwoForm()
	carrieroneform = CarrierOneForm()
	carriertwoform = CarrierTwoForm()
	upsoneform = UpsOneForm()
	return render(request, 'tek_view/sala-ups.html', {'stulzoneform': stulzoneform, 'stulztwoform': stulztwoform, 'carrieroneform': carrieroneform, 'carriertwoform': carriertwoform, 'upsoneform': upsoneform})


def grupos_electrogenos(request):
	return render(request, 'tek_view/grupos_electrogenos')
	

# |------------DATA HANDLERS------------|


def data_stulz_one(request):
	form = 	StulzOneForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/sala_ups')


def data_stulz_two(request):
	form = 	StulzTwoForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/sala_ups')