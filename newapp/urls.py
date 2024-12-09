from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('index', views.index),
    path('dash', views.dashboard, name= 'dashboard'),
    path('add/', views.add_journal_entry, name='add_journal_entry'),
    path('dashboard/', views.dashboard, name='dash'),
    path('journal/', views.journal, name='journal'),
    path('mindfull/', views.mindfull, name='mindfull'),
    path('profile/', views.profile, name='profile'),
]


