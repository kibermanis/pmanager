from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WaterCounterReadings, WaterCounterCategory
from django.utils.timezone import datetime
# from django.http import HttpResponse



# @login_required(login_url='login')

def home(request):
    if request.method == 'POST':
        readings = WaterCounterReadings()
        readings.water_counter_num = WaterCounterCategory.objects.get(water_counter_num=request.POST['counter_nr'])
        readings.water_counter_reading = request.POST['reading']
        readings.water_counter_readings_current_date = datetime.now()
        # readings.water_counter_readings_date_on = datetime.now()
        readings.save()  # šī rinda ieli db
        wcounters = WaterCounterCategory.objects
        return render(request, 'water.html', {'wconters': wcounters})

    else:
        wcounters = WaterCounterCategory.objects
        return render(request, 'water.html', {'wconters': wcounters})







