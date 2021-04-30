from django.db import models

#Clima models
class Stulz_one(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Stulz_two(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chiller_uniflair(models.Model):
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    compressor_one = models.BooleanField(blank=True, null=True)
    compressor_two = models.BooleanField(blank=True, null=True)
    compressor_three = models.BooleanField(blank=True, null=True)
    compressor_four = models.BooleanField(blank=True, null=True)
    eva_pressure_circuit_one = models.FloatField()
    eva_pressure_circuit_two = models.FloatField()
    cond_pressure_circuit_one = models.FloatField()
    cond_pressure_circuit_two = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chiller_climavenetta(models.Model):
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    compressor_one = models.BooleanField(blank=True, null=True)
    compressor_two = models.BooleanField(blank=True, null=True)
    compressor_three = models.BooleanField(blank=True, null=True)
    compressor_four = models.BooleanField(blank=True, null=True)
    eva_pressure_circuit_one = models.FloatField()
    eva_pressure_circuit_two = models.FloatField()
    cond_pressure_circuit_one = models.FloatField()
    cond_pressure_circuit_two = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Carrier_one(models.Model):
    temperature = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Carrier_two(models.Model):
    temperature = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pump_one(models.Model):
    pressure_out = models.FloatField(default=0)
    pressure_in= models.FloatField(default=0)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Pump_two(models.Model):
    pressure_out = models.FloatField(default=0)
    pressure_in= models.FloatField(default=0)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pump_three(models.Model):
    pressure_out = models.FloatField(default=0)
    pressure_in= models.FloatField(default=0)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#energy models

class UPS_one(models.Model):
    volt_in_u = models.FloatField()
    volt_in_v = models.FloatField()
    volt_in_w = models.FloatField()
    curr_in_u = models.FloatField()
    curr_in_v = models.FloatField()
    curr_in_w = models.FloatField()
    frecuency_in = models.FloatField()
    volt_out_u = models.FloatField()
    volt_out_v = models.FloatField()
    volt_out_w = models.FloatField()
    curr_out_u = models.FloatField()
    curr_out_v = models.FloatField()
    curr_out_w = models.FloatField()
    frecuency_out = models.FloatField()
    battery_volt = models.FloatField()
    battery_curr = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    last_event = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UPS_two(models.Model):
    volt_in_u = models.FloatField()
    volt_in_v = models.FloatField()
    volt_in_w = models.FloatField()
    curr_in_u = models.FloatField()
    curr_in_v = models.FloatField()
    curr_in_w = models.FloatField()
    frecuency_in = models.FloatField()
    volt_out_u = models.FloatField()
    volt_out_v = models.FloatField()
    volt_out_w = models.FloatField()
    curr_out_u = models.FloatField()
    curr_out_v = models.FloatField()
    curr_out_w = models.FloatField()
    frecuency_out = models.FloatField()
    battery_volt = models.FloatField()
    battery_curr = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    last_event = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

choices  = [('run', 'run'),('auto', 'auto'),('stop', 'stop'),]
class GE_one(models.Model):
    state = models.CharField(max_length=50, choices = choices)
    temperature = models.FloatField()
    battery_volt = models.FloatField()
    hours_running = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GE_two(models.Model):
    state = models.CharField(max_length=50, choices = choices)
    temperature = models.FloatField()
    battery_volt = models.FloatField()
    hours_running = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Power(models.Model):
    kva = models.FloatField()
    kw = models.FloatField()
    kvar = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Alert(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    