from django.urls import path
from . import views  # Make sure views is imported correctly

urlpatterns = [
    path('', views.bin_list, name='bin_list'),  # This is where you link the view to the URL pattern
]
