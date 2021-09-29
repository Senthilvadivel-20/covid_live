from django.shortcuts import render
from covid import  scrap


def home(request):
    cases=scrap.covid()
    Cases,Death,Recovery=cases
    # chart=scrap.cases_plot()
    # scrap.cases_plot()
    # scrap.death_plot()
    # scrap.recovery_plot()
    return render(request,'home.html',locals())

def world_map(request):
    return render(request,'map.html')


