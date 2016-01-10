from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app.distance_calc import haversine
from app.models import Location

# Create your views here.
@csrf_exempt
def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        if 'coords' in request.POST:
            coordinates = request.POST['coords']
            lat, lon = coordinates.split(',')
            all_locations = Location.objects.all()
            distances = []
            for location in all_locations:
                distance = haversine(
                    float(lon),
                    float(lat),
                    location.lon,
                    location.lat)
                json_location = {
                    'lat': location.lat,
                    'lon': location.lon,
                    'label': location.label,
                    'book': location.book.name,
                    'quotes': list(location.book.quote_set.values_list('text', flat=True))
                }
                distances.append([distance, json_location])
            distances = sorted(distances, key=lambda x: x[0])

            return JsonResponse({'distances': [i[1] for i in distances[:5]]})
    return HttpResponse('FAIL!!!!!')
