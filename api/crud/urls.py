from django.urls import re_path
from .views import *

urlpatterns = [ 
    re_path(r'^location/$', location_list, name='location-list'),
]