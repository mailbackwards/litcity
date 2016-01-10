import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app.distance_calc import haversine
from app.models import Location

# Create your views here.
@csrf_exempt
def wander_view(request):
    return render(request, 'wander.html')

@csrf_exempt
def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        if 'coords' in request.POST:
            coordinates = request.POST['coords']
            user_lat, user_lon = [float(i) for i in coordinates.split(',')]
            distance_from_origin = lambda loc: haversine(
                user_lon, user_lat, loc['lon'], loc['lat'])
            all_locations = Location.objects.select_related('book').prefetch_related('book__quote_set', 'quotes')
            def get_quote(location):
                try:
                    return random.choice(location.quotes.all()).text
                except IndexError:
                    return random.choice(location.book.quote_set.all()).text
            results = [{
                'lat': location.lat,
                'lon': location.lon,
                'label': location.label,
                'book': location.book.name,
                'author': location.book.author,
                'quote': get_quote(location)
            } for location in all_locations]
            sorted_results = sorted(results, key=distance_from_origin)[:5]

            return JsonResponse({'results': sorted_results})
    return HttpResponse('FAIL!!!!!')
