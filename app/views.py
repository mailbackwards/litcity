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
            # distance_from_origin = lambda loc: haversine(
            #     user_lon, user_lat, loc['lon'], loc['lat'])
            all_locations = Location.objects.filter(approved=True).select_related('book').prefetch_related('book__quote_set', 'quotes')
            def get_quote(location):
                if location.quotes.filter(approved=True):
                    q = random.choice(location.quotes.filter(approved=True))
                elif location.book.quote_set.filter(approved=True):
                    q = random.choice(location.book.quote_set.filter(approved=True))
                else:
                    q = None
                return q.text if q is not None else ''
            results = [{
                'lat': location.lat,
                'lon': location.lon,
                'label': location.label,
                'book': location.book.name,
                'author': location.book.author,
                'quote': get_quote(location)
            } for location in all_locations]
            # results = sorted(results, key=distance_from_origin)

            return JsonResponse({'results': results})
    return HttpResponse('FAIL!!!!!')
