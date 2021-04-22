from django.urls import path
from . import views

urlpatterns = [
	path('',  views.index, name="landing-page"),
	path('main',  views.main, name="main-page"),
	path('logout',  views.logout, name="logout"),
	path('choose_view',  views.choose_view, name="choose_view"),
]