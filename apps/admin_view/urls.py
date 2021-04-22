from django.urls import path
from . import views

urlpatterns = [
	path('admin_view',  views.admin_view, name="admin_view"),
	path('stulz_one_data',  views.stulz_one_data, name="stulz_one_data"),
]