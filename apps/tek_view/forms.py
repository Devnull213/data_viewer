from django import forms
from .models import *
import re

#SALA UPS

class StulzOneForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'alarmado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Stulz_one

        fields = [
            'state',
            'temperature',
            'humidity',
            'comment',
        ]

        labels = {
            'temperature': 'Temperatura',
            'humidity': 'Humedad',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }

        
class StulzTwoForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'alarmado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Stulz_two

        fields = [
            'state',
            'temperature',
            'humidity',
            'comment',
        ]

        labels = {
            'temperature': 'Temperatura',
            'humidity': 'Humedad',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }



class CarrierOneForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'alarmado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Carrier_one 

        fields = [
            'state',
            'temperature',
            'comment',
        ]

        labels = {
            'temperature': 'Temperatura',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }




class CarrierTwoForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'alarmado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Carrier_two

        fields = [
            'state',
            'temperature',
            'comment',
        ]

        labels = {
            'temperature': 'Temperatura',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }


class UpsOneForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'alarmado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = UPS_one

        fields = [
            'volt_in_u',
            'volt_in_v',
            'volt_in_w',
            'curr_in_u',
            'curr_in_v',
            'curr_in_w',
            'frecuency_in',
            'volt_out_u',
            'volt_out_v',
            'volt_out_w',
            'curr_out_u',
            'curr_out_v',
            'curr_out_w',
            'frecuency_out',
            'battery_volt',
            'battery_curr',
            'comment',
        ]

        labels = {
            'volt_in_u': 'Voltaje in U',
            'volt_in_v': 'Voltaje in V',
            'volt_in_w': 'Voltaje in W',
            'curr_in_u': 'Corriente in U',
            'curr_in_v': 'Corriente in V',
            'curr_in_w': 'Corriente in W',
            'frecuency_in': 'Frecuencia in',
            'volt_out_u': 'Voltaje out U',
            'volt_out_v': 'Voltaje out V',
            'volt_out_w': 'Voltaje out W',
            'curr_out_u': 'Corriente out U',
            'curr_out_v': 'Corriente out V',
            'curr_out_w': 'Corriente out W',
            'frecuency_out': 'Frecuencia out',
            'battery_volt': 'Voltaje celda',
            'battery_curr': 'Corriente celda',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }



class UpsTwoForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'alarmado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = UPS_two

        fields = [
            'volt_in_u',
            'volt_in_v',
            'volt_in_w',
            'curr_in_u',
            'curr_in_v',
            'curr_in_w',
            'frecuency_in',
            'volt_out_u',
            'volt_out_v',
            'volt_out_w',
            'curr_out_u',
            'curr_out_v',
            'curr_out_w',
            'frecuency_out',
            'battery_volt',
            'battery_curr',
            'comment',
        ]

        labels = {
            'volt_in_u': 'Voltaje in U',
            'volt_in_v': 'Voltaje in V',
            'volt_in_w': 'Voltaje in W',
            'curr_in_u': 'Corriente in U',
            'curr_in_v': 'Corriente in V',
            'curr_in_w': 'Corriente in W',
            'frecuency_in': 'Frecuencia in',
            'volt_out_u': 'Voltaje out U',
            'volt_out_v': 'Voltaje out V',
            'volt_out_w': 'Voltaje out W',
            'curr_out_u': 'Corriente out U',
            'curr_out_v': 'Corriente out V',
            'curr_out_w': 'Corriente out W',
            'frecuency_out': 'Frecuencia out',
            'battery_volt': 'Voltaje celda',
            'battery_curr': 'Corriente celda',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }



class ChillerUniForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'apagado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Chiller_uniflair

        fields = [
            'temp_in',
            'temp_out',
            'compressor_one',
            'compressor_two',
            'compressor_three',
            'compressor_four',
            'eva_pressure_circuit_one',
            'eva_pressure_circuit_two',
            'cond_pressure_circuit_one',
            'cond_pressure_circuit_two',
            'comment' 
        ]

        labels = {
            'temp_in': 'Entrada',
            'temp_out': 'Salida',
            'compressor_one': 'Compresor uno',
            'compressor_two': 'Compresor dos',
            'compressor_three': 'Compresor tres',
            'compressor_four': 'Compresor cuatro',
            'eva_pressure_circuit_one': 'Presión evaporación c-1',
            'eva_pressure_circuit_two': 'Presión evaporacion c-2',
            'cond_pressure_circuit_one': 'Presión condesación c-1',
            'cond_pressure_circuit_two': 'Presión condensación c-2',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }


class ChillerClimaform(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'apagado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Chiller_climavenetta

        fields = [
            'temp_in',
            'temp_out',
            'compressor_one',
            'compressor_two',
            'compressor_three',
            'compressor_four',
            'eva_pressure_circuit_one',
            'eva_pressure_circuit_two',
            'cond_pressure_circuit_one',
            'cond_pressure_circuit_two',
            'comment' 
        ]

        labels = {
            'temp_in': 'Entrada',
            'temp_out': 'Salida',
            'compressor_one': 'Compresor uno',
            'compressor_two': 'Compresor dos',
            'compressor_three': 'Compresor tres',
            'compressor_four': 'Compresor cuatro',
            'eva_pressure_circuit_one': 'Presión evaporación c-1',
            'eva_pressure_circuit_two': 'Presión evaporacion c-2',
            'cond_pressure_circuit_one': 'Presión condesación c-1',
            'cond_pressure_circuit_two': 'Presión condensación c-2',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }
        
class PumpOneForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'apagado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Pump_one

        fields = [
            'pressure_out',
            'pressure_in',
            'comment' 
        ]

        labels = {
            'pressure_out': 'Presión de bombeo',
            'pressure_in': 'Presión de retorno',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }


class PumpTwoForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'apagado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Pump_two

        fields = [
            'pressure_out',
            'pressure_in',
            'comment' 
        ]

        labels = {
            'pressure_out': 'Presión de bombeo',
            'pressure_in': 'Presión de retorno',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }


class PumpThreeForm(forms.ModelForm):
    choices = [('0', 'encendido'), ('2', 'apagado')]
    state = forms.ChoiceField(label = 'Estado',widget= forms.RadioSelect, choices=choices)
    class Meta:
        model = Pump_three

        fields = [
            'pressure_out',
            'pressure_in',
            'comment' 
        ]

        labels = {
            'pressure_out': 'Presión de bombeo',
            'pressure_in': 'Presión de retorno',
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }



class GEOneForm(forms.ModelForm):
    class Meta:
        model = GE_one

        fields = [
            'state',
            'temperature',
            'battery_volt', 
            'hours_running', 
            'comment' 
        ]

        labels = {
            'state': 'Modo',
            'temperature': 'Temperatura',
            'battery_volt': 'Voltaje Batería', 
            'hours_running': 'Horas de uso acumuladas', 
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }


class GETwoForm(forms.ModelForm):
    class Meta:
        model = GE_two

        fields = [
            'state',
            'temperature',
            'battery_volt', 
            'hours_running', 
            'comment' 
        ]

        labels = {
            'state': 'Modo',
            'temperature': 'Temperatura',
            'battery_volt': 'Voltaje Batería', 
            'hours_running': 'Horas de uso acumuladas', 
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }


class PowerForm(forms.ModelForm):
    class Meta:
        model = Power 

        fields = [
            'kva',
            'kw',
            'kvar', 
            'comment' 
        ]

        labels = {
            'kva': 'KVA',
            'kw': 'KW',
            'kvar': 'KVAR', 
            'comment': 'Comentarios (opcional)',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': '24', 'rows': '5'})
        }