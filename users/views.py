from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from water.models import WaterCounterCategory


def loginuser(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None: #vai esam atraduši lietotāju no iepriekšējās rindiņas?
            auth.login(request, user) #veicam lietotāja ielogošanu
            wcounters = WaterCounterCategory.objects
            return render(request, 'water.html', {'wconters': wcounters})
        else: # ja lietotājs db netika atrasts,     tad
            return render(request, 'login.html', {'error': 'Lietotājs netika atrasts vai parole nav pareiza!!!!' })
    else:
        return render(request, 'login.html')

def logoutuser(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'login.html')
    else:
        return HttpResponse ('Nav izlogojies')