from django.urls import path
from . import views

urlpatterns = [
	path('admin_view',  views.admin_view, name="admin_view"),
	path('date_config',  views.date_config, name="date_config"),
	path('stulz_one_data',  views.stulz_one_data, name="stulz_one_data"),
	path('stulz_two_data',  views.stulz_two_data, name="stulz_two_data"),
]