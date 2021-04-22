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
	path('data_stulz_one',  views.data_stulz_one, name="data_stulz_one"),
]