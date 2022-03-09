from django.urls import path
from .views import homeView
app_name = 'reports'
urlpatterns = [
    path('', homeView, name='home')
]
