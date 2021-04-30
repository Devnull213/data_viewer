from django.shortcuts import render, redirect, HttpResponse
from .forms import * 
from apps.log_register.views import *

def tech_view(request):
	return render(request, 'tek_view/main.html' )


def data_center(request):
	powerform = PowerForm()
	return render(request, 'tek_view/data-center.html', {'powerform': powerform})


def azotea(request):
	chilleruniflairform = ChillerUniForm()
	chillerclimavenettaform = ChillerClimaform()
	pumponeform = PumpOneForm()
	pumptwoform = PumpTwoForm()
	pumpthreeform = PumpThreeForm()
	return render(request, 'tek_view/azotea.html', {'chilleruniflairform': chilleruniflairform, 'chillerclimavenettaform': chillerclimavenettaform, 'pumponeform': pumponeform,'pumptwoform': pumptwoform,'pumpthreeform': pumpthreeform, })


def sala_ups(request):
	stulzoneform = StulzOneForm()
	stulztwoform = StulzTwoForm()
	carrieroneform = CarrierOneForm()
	carriertwoform = CarrierTwoForm()
	upsoneform = UpsOneForm()
	upstwoform = UpsTwoForm()
	return render(request, 'tek_view/sala-ups.html', {'stulzoneform': stulzoneform, 'stulztwoform': stulztwoform, 'carrieroneform': carrieroneform, 'carriertwoform': carriertwoform, 'upsoneform': upsoneform, 'upstwoform': upstwoform})


def grupos_electrogenos(request):
	geoneform = GEOneForm()
	getwoform = GETwoForm()
	return render(request, 'tek_view/grupos-electrogenos.html', {'geoneform': geoneform, 'getwoform': getwoform})


def create_alert(request):
	if request.method == 'GET':
		form = CreateAlertForm()
	else:
		form = CreateAlertForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/tek_view/tech_view')
	return render(request, 'tek_view/create-alarm.html', {'form': form})
	

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


def data_carrier_one(request):
	form = 	CarrierOneForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/sala_ups')


def data_carrier_two(request):
	form = 	CarrierTwoForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/sala_ups')


def data_ups_one(request):
	form = 	UpsOneForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/sala_ups')


def data_ups_two(request):
	form = 	UpsTwoForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/sala_ups')


def data_chiller_uniflair(request):
	form = 	ChillerUniForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/azotea')


def data_chiller_climavenetta(request):
	form = 	ChillerClimaform(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/azotea')


def data_pump_one(request):
	form = 	PumpOneForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/azotea')


def data_pump_two(request):
	form = 	PumpTwoForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/azotea')


def data_pump_three(request):
	form = 	PumpThreeForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/azotea')


def data_ge_one(request):
	form = 	GEOneForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/grupos_electrogenos')


def data_ge_two(request):
	form = 	GETwoForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/grupos_electrogenos')


def data_power(request):
	form = 	PowerForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect('/tek_view/data_center')