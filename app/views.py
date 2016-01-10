from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        if 'coords' in request.POST:
            coordinates = request.POST['coords']
            return HttpResponse('success')
    return HttpRepsonse('FAIL!!!!!')
