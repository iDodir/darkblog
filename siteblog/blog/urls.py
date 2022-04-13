from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<slug:slug>/', views.get_category, name='category'),
]
