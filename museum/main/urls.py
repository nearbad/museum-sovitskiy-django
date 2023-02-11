from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('museum_of_Nukus/', nks_museum, name='nks_museum'),
    path('collections/', collections, name='collections'),
    path('sources/', sources, name='sources'),
    path('catalogue/', catalogue, name='catalogue'),
    path('credits/', credits, name='credits'),
    path('copyright/', copyright, name='copyright'),
    path('contact/', contact, name='contact'),
]