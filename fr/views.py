from django.shortcuts import render
from .models import mosque_main
from django.http import JsonResponse
# Create your views here.

def index(request):
	return render(request, 'fr/testing.html', { })


def mosques(request):

	m_list = mosque_main.objects.all()

	data = list(mosque_main.objects.values())

	return JsonResponse(data, safe=False)



	# for k in m_list:
	# 	print(k.name)

	# return render(request, 'fr/getcheck.html', { 'mosque_list' : m_list ,})
