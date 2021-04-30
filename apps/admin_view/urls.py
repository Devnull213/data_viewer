from django.urls import path
from . import views

urlpatterns = [
	path('admin_view',  views.admin_view, name="admin_view"),
	path('date_config',  views.date_config, name="date_config"),
	path('stulz_one_data',  views.stulz_one_data, name="stulz_one_data"),
	path('stulz_two_data',  views.stulz_two_data, name="stulz_two_data"),
	path('carrier_one_data',  views.carrier_one_data, name="carrier_one_data"),
	path('carrier_two_data',  views.carrier_two_data, name="carrier_two_data"),
	path('ups_one_data',  views.ups_one_data, name="ups_one_data"),
	path('ups_two_data',  views.ups_two_data, name="ups_two_data"),
	path('chiller_uniflair_data',  views.chiller_uniflair_data, name="chiller_uniflair_data"),
	path('chiller_climavenetta_data',  views.chiller_climavenetta_data, name="chiller_climavenetta_data"),
	path('pump_one_data',  views.pump_one_data, name="pump_one_data"),
	path('pump_two_data',  views.pump_two_data, name="pump_two_data"),
	path('pump_three_data',  views.pump_three_data, name="pump_three_data"),
	path('ge_one_data',  views.ge_one_data, name="ge_one_data"),
	path('ge_two_data',  views.ge_two_data, name="ge_two_data"),
	path('power_data',  views.power_data, name="power_data"),
	path('alert_messages',  views.alert_messages, name="alert_messages"),
]