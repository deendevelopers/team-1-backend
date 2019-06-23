from django.shortcuts import render
from .models import mosque_main, Mosque_Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	return render(request, 'fr/testing.html', { })

def mosques_list(request):
	data = list(mosque_main.objects.values())
	return JsonResponse(data, safe=False)

def mosques_detail(request, mosque_id):
	data = list(mosque_main.objects.filter(id=mosque_id).values())[0]
	return JsonResponse(data,safe=False)


def mosque_detail_comment(request,mosque_id):
	if request.method == "GET":
		comment_data = list(Mosque_Comment.objects.filter(mosque_id=mosque_id).values())
		return JsonResponse(comment_data,safe=False)
	elif request.method == "POST":
		category_name = request.POST.get("category_name")
		comment  = request.POST.get("comment")
		comment_type = request.POST.get("comment_type")
		comment_object = Mosque_Comment(user_id=1,mosque_id=mosque_id,category_name=category_name, comment=comment, comment_type=comment_type)
		comment_object.save()
		comment_data = list(Mosque_Comment.objects.filter(mosque_id=mosque_id).values())
		return JsonResponse(comment_data,safe=False)
