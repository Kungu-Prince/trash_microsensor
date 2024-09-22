from django.shortcuts import render
from .models import Bin  # Import the Bin model if you're using it

# The bin_list view function
def bin_list(request):
    bins = Bin.objects.all()  # Query to get all bins (if you have the Bin model)
    return render(request, 'bin_management/bin_list.html', {'bins': bins})
