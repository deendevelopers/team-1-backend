from django.shortcuts import render
from .models import mosque_main
from django.http import JsonResponse
# Create your views here.

def index(request):
	return render(request, 'fr/testing.html', { })


def mosques_list(request):
	data = list(mosque_main.objects.values())
	return JsonResponse(data, safe=False)


def mosques_detail(request, mosque_id):
	data = list(mosque_main.objects.filter(id=mosque_id).values())


	return JsonResponse(data,safe=False)