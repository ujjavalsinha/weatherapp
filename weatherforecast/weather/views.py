from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from .forms import CityForm
from weather.models import City
from django.utils import timezone

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f091951f664ef05836986baedd47f099'

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

        cities = City.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[0:1]
        weather_data = []


        for city in cities:
            r = requests.get(url.format(city)).json()
            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']
            }
            weather_data.append(city_weather)


        context = {'weather_data':weather_data, 'form':form}
        return render(request, 'index.html', context)

        form = CityForm
    else:

        form = CityForm
        return render(request, 'index.html', {'form':form} )
