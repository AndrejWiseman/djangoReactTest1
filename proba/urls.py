from django.urls import path, include
from .views import home

app_name = 'proba'

urlpatterns = [
    path('', home, name='home')
]

