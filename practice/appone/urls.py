from django.urls import path,include
from appone import views

app_name = 'appone'

urlpatterns = [
   path('join/', views.form_name_view, name='join'),
   path('members/',views.members, name='members')
]
