from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('feature/', views.feature, name='feature'),
	path('post/<slug:slug>', views.post, name='post'),

]
