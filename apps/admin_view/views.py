from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from apps.tek_view.models import  Alert
from apps.tek_view.views import *

def admin_view(request):
	current_date = datetime.now()
	current_date = current_date.strftime('%Y-%m-%d')
	return render(request, 'admin_view/main.html', {'date': current_date})

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


def carrier_one_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	stulz_date = Carrier_one.objects.all().filter(created_at__date=(the_date))
	temp = []
	for temper in stulz_date:
		temp.append(temper.temperature)
	data = {
		'temp': temp,
		'labels': labels,
	}
	return JsonResponse(data)


def carrier_two_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	stulz_date = Carrier_two.objects.all().filter(created_at__date=(the_date))
	temp = []
	for temper in stulz_date:
		temp.append(temper.temperature)
	data = {
		'temp': temp,
		'labels': labels,
	}
	return JsonResponse(data)


def ups_one_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	ups_data = UPS_one.objects.all().filter(created_at__date=(the_date))
	volt_u_in = []
	volt_v_in = []
	volt_w_in = []
	curr_u_in = []
	curr_v_in = []
	curr_w_in = []
	volt_u_out = []
	volt_v_out = []
	volt_w_out = []
	curr_u_out = []
	curr_v_out = []
	curr_w_out = []
	for volt in ups_data:
		volt_u_in.append(volt.volt_in_u)

	for volt in ups_data:
		volt_v_in.append(volt.volt_in_v)

	for volt in ups_data:
		volt_w_in.append(volt.volt_in_w)

	for volt in ups_data:
		volt_u_out.append(volt.volt_out_u)

	for volt in ups_data:
		volt_v_out.append(volt.volt_out_v)

	for volt in ups_data:
		volt_w_out.append(volt.volt_out_w)

	for curr in ups_data:
		curr_u_in.append(curr.curr_in_u)

	for curr in ups_data:
		curr_v_in.append(curr.curr_in_v)

	for curr in ups_data:
		curr_w_in.append(curr.curr_in_w)

	for curr in ups_data:
		curr_u_out.append(curr.curr_out_u)

	for curr in ups_data:
		curr_v_out.append(curr.curr_out_v)

	for curr in ups_data:
		curr_w_out.append(curr.curr_out_w)

	data = {
		'volt_u_in': volt_u_in,
		'volt_v_in': volt_v_in,
		'volt_w_in': volt_w_in,
		'volt_u_out': volt_u_out,
		'volt_v_out': volt_v_out,
		'volt_w_out': volt_w_out,
		'curr_u_in': curr_u_in,
		'curr_v_in': curr_v_in,
		'curr_w_in': curr_w_in,
		'curr_u_out': curr_u_out,
		'curr_v_out': curr_v_out,
		'curr_w_out': curr_w_out,
		'labels': labels,
	}
	return JsonResponse(data)


def ups_two_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	ups_data = UPS_two.objects.all().filter(created_at__date=(the_date))
	volt_u_in = []
	volt_v_in = []
	volt_w_in = []
	curr_u_in = []
	curr_v_in = []
	curr_w_in = []
	volt_u_out = []
	volt_v_out = []
	volt_w_out = []
	curr_u_out = []
	curr_v_out = []
	curr_w_out = []
	for volt in ups_data:
		volt_u_in.append(volt.volt_in_u)

	for volt in ups_data:
		volt_v_in.append(volt.volt_in_v)

	for volt in ups_data:
		volt_w_in.append(volt.volt_in_w)

	for volt in ups_data:
		volt_u_out.append(volt.volt_out_u)

	for volt in ups_data:
		volt_v_out.append(volt.volt_out_v)

	for volt in ups_data:
		volt_w_out.append(volt.volt_out_w)

	for curr in ups_data:
		curr_u_in.append(curr.curr_in_u)

	for curr in ups_data:
		curr_v_in.append(curr.curr_in_v)

	for curr in ups_data:
		curr_w_in.append(curr.curr_in_w)

	for curr in ups_data:
		curr_u_out.append(curr.curr_out_u)

	for curr in ups_data:
		curr_v_out.append(curr.curr_out_v)

	for curr in ups_data:
		curr_w_out.append(curr.curr_out_w)

	data = {
		'volt_u_in': volt_u_in,
		'volt_v_in': volt_v_in,
		'volt_w_in': volt_w_in,
		'volt_u_out': volt_u_out,
		'volt_v_out': volt_v_out,
		'volt_w_out': volt_w_out,
		'curr_u_in': curr_u_in,
		'curr_v_in': curr_v_in,
		'curr_w_in': curr_w_in,
		'curr_u_out': curr_u_out,
		'curr_v_out': curr_v_out,
		'curr_w_out': curr_w_out,
		'labels': labels,
	}
	return JsonResponse(data)


def chiller_climavenetta_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	chiller_data = Chiller_climavenetta.objects.all().filter(created_at__date=(the_date))
	temp_in = []
	temp_out = []
	eva_pressure_c1 = []
	eva_pressure_c2 = []
	cond_pressure_c1 = []
	cond_pressure_c2 = []

	for data in chiller_data:
		temp_in.append(data.temp_in)

	for data in chiller_data:
		temp_out.append(data.temp_out)

	for data in chiller_data:
		eva_pressure_c1.append(data.eva_pressure_circuit_one)

	for data in chiller_data:
		eva_pressure_c2.append(data.eva_pressure_circuit_two)

	for data in chiller_data:
		cond_pressure_c1.append(data.cond_pressure_circuit_one)

	for data in chiller_data:
		cond_pressure_c2.append(data.cond_pressure_circuit_two)

	data = {
		'temp_in': temp_in,
		'temp_out': temp_out,
		'eva_pressure_c1': eva_pressure_c1,
		'eva_pressure_c2': eva_pressure_c2,
		'cond_pressure_c1': cond_pressure_c1,
		'cond_pressure_c2': cond_pressure_c2,
		'labels': labels,
	}
	return JsonResponse(data)


def chiller_uniflair_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	chiller_data = Chiller_uniflair.objects.all().filter(created_at__date=(the_date))
	temp_in = []
	temp_out = []
	eva_pressure_c1 = []
	eva_pressure_c2 = []
	cond_pressure_c1 = []
	cond_pressure_c2 = []

	for data in chiller_data:
		temp_in.append(data.temp_in)

	for data in chiller_data:
		temp_out.append(data.temp_out)

	for data in chiller_data:
		eva_pressure_c1.append(data.eva_pressure_circuit_one)

	for data in chiller_data:
		eva_pressure_c2.append(data.eva_pressure_circuit_two)

	for data in chiller_data:
		cond_pressure_c1.append(data.cond_pressure_circuit_one)

	for data in chiller_data:
		cond_pressure_c2.append(data.cond_pressure_circuit_two)

	data = {
		'temp_in': temp_in,
		'temp_out': temp_out,
		'eva_pressure_c1': eva_pressure_c1,
		'eva_pressure_c2': eva_pressure_c2,
		'cond_pressure_c1': cond_pressure_c1,
		'cond_pressure_c2': cond_pressure_c2,
		'labels': labels,
	}
	return JsonResponse(data)


def pump_one_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	pump_data = Pump_one.objects.all().filter(created_at__date=(the_date))
	pressure_out = []
	pressure_in = []
	for data in pump_data:
		pressure_out.append(data.pressure_out)
	for data in pump_data:
		pressure_in.append(data.pressure_in)
	data = {
		'pressure_out': pressure_out,
		'pressure_in': pressure_in,
		'labels': labels,
	}
	return JsonResponse(data)


def pump_two_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	pump_data = Pump_two.objects.all().filter(created_at__date=(the_date))
	pressure_out = []
	pressure_in = []
	for data in pump_data:
		pressure_out.append(data.pressure_out)
	for data in pump_data:
		pressure_in.append(data.pressure_in)
	data = {
		'pressure_out': pressure_out,
		'pressure_in': pressure_in,
		'labels': labels,
	}
	return JsonResponse(data)


def pump_three_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	pump_data = Pump_three.objects.all().filter(created_at__date=(the_date))
	pressure_out = []
	pressure_in = []
	for data in pump_data:
		pressure_out.append(data.pressure_out)
	for data in pump_data:
		pressure_in.append(data.pressure_in)
	data = {
		'pressure_out': pressure_out,
		'pressure_in': pressure_in,
		'labels': labels,
	}
	return JsonResponse(data)


def ge_one_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	ge_data = GE_one.objects.all().filter(created_at__date=(the_date))
	temp = []
	volt = []
	for data in ge_data:
		temp.append(data.temperature)
	for data in ge_data:
		volt.append(data.battery_volt)
	data = {
		'temp': temp,
		'volt': volt,
		'labels': labels,
	}
	return JsonResponse(data)


def ge_two_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	ge_data = GE_two.objects.all().filter(created_at__date=(the_date))
	temp = []
	volt = []
	for data in ge_data:
		temp.append(data.temperature)
	for data in ge_data:
		volt.append(data.battery_volt)
	data = {
		'temp': temp,
		'volt': volt,
		'labels': labels,
	}
	return JsonResponse(data)


def power_data(request):
	labels = ['Checklist #1','Checklist #2','Checklist #3','Checklist #4','Checklist #5','Checklist #6','Checklist #7','Checklist #8',]
	power_data = Power.objects.all().filter(created_at__date=(the_date))
	kva_total = 0
	kw_total = 0
	kvar_total = 0
	kva = []
	kw = []
	kvar = []

	for data in power_data:
		kva_total += data.kva 
		kva.append(data.kva)
	kva_total = kva_total #/ len(kva)

	for data in power_data:
		kw_total += data.kw 
		kw.append(data.kw)
	kw_total = kw_total #/ len(kw)

	for data in power_data:
		kvar_total += data.kvar 
		kvar.append(data.kvar)

	kvar_total = kvar_total #/ len(kvar)

	data = {
		'kva': kva,
		'kva_total': kva_total,
		'kw': kw,
		'kw_total': kw_total,
		'kvar': kvar,
		'kvar_total': kvar_total,
		'labels': labels,
	}
	return JsonResponse(data)

def alert_messages(request):
	alerts = Alert.objects.all()
	return render(request, 'admin_view/view-alerts.html', {'alert': alerts})
