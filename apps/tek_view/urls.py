from django.urls import path
from . import views

urlpatterns = [
	path('tech_view',  views.tech_view, name="tech_view"),
	path('sala_ups',  views.sala_ups, name="sala_ups"),
	path('grupos_electrogenos',  views.grupos_electrogenos, name="grupos_electrogenos"),
	path('azotea',  views.azotea, name="azotea"),
	path('data_center',  views.data_center, name="data_center"),

	#|----------------------------Data paths----------------------------|

	path('data_stulz_one',  views.data_stulz_one, name="data_stulz_one"),
	path('data_stulz_two',  views.data_stulz_two, name="data_stulz_two"),
	path('data_carrier_one',  views.data_carrier_one, name="data_carrier_one"),
	path('data_carrier_two',  views.data_carrier_two, name="data_carrier_two"),
	path('data_ups_one',  views.data_ups_one, name="data_ups_one"),
	path('data_ups_two',  views.data_ups_two, name="data_ups_two"),
	path('data_chiller_uniflair',  views.data_chiller_uniflair, name="data_chiller_uniflair"),
	path('data_chiller_climavenetta',  views.data_chiller_climavenetta, name="data_chiller_climavenetta"),
	path('data_pump_one',  views.data_pump_one, name="data_pump_one"),
	path('data_pump_two',  views.data_pump_two, name="data_pump_two"),
	path('data_pump_three',  views.data_pump_three, name="data_pump_three"),
	path('data_ge_one',  views.data_ge_one, name="data_ge_one"),
	path('data_ge_two',  views.data_ge_two, name="data_ge_two"),
	path('data_power',  views.data_power, name="data_power"),
	path('create_alert',  views.create_alert, name="create_alert"),
]