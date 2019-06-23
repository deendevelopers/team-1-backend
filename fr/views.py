from django.shortcuts import render
from .models import mosque_main, Comment_Vote, Vote_Track
from .models import mosque_main, Mosque_Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.

def index(request):
	return render(request, 'fr/testing.html', { })

def mosques_list(request):
	data = list(mosque_main.objects.values())
	return JsonResponse(data, safe=False)

def mosques_detail(request, mosque_id):
	data = list(mosque_main.objects.filter(id=mosque_id).values())[0]
	return JsonResponse(data,safe=False)

def comment_vote(request, comment_id):

	if request.method == "POST":
		uid_voter = request.POST.get("user_id_voter")
		vtype = request.POST.get("type")

		v_track = Vote_Track.objects.filter(user_id_voter=uid_voter, comment_id=comment_id).order_by('-timestamp').values_list('vote_type', flat=True)[0]

		if v_track == 'up' and vtype == 'up':
			return JsonResponse("{'denied' : 'up'}", safe=False)
		elif v_track == 'down' and vtype == 'down':
			return JsonResponse("{'denied' : 'down'}", safe=False)

		v_check = Comment_Vote.objects.filter(comment_id=comment_id).values_list('vote_num', flat=True)[0]

		if vtype == 'up':
			v_check += 1
		elif vtype == 'down':
			v_check -= 1

		vote_change = Comment_Vote(comment_id=comment_id, vote_num=v_check)
		vote_change.save()

		track_user_vote  = Vote_Track(user_id_voter=uid_voter, comment_id=comment_id, vote_type=vtype)
		track_user_vote.save()

		return JsonResponse("{'change' : '{}'}".format(v_check), safe=False)



def mosque_detail_comment(request,mosque_id):
	if request.method == "GET":


		q = """
			select mc.*, cv.vote_num from fr_mosque_comment mc
			left join fr_comment_vote cv
			on mc.id = cast(cv.comment_id as integer)
			"""

		comment_data = serializers.serialize('json', Mosque_Comment.objects.raw(q))


		# comment_data = list(Mosque_Comment.objects.filter(mosque_id=mosque_id).prefetch_related(
  #       'id', 'comment_id').values())


		return JsonResponse(comment_data,safe=False)
	elif request.method == "POST":
		category_name = request.POST.get("category_name")
		comment  = request.POST.get("comment")
		comment_type = request.POST.get("comment_type")
		comment_object = Mosque_Comment(user_id=1,mosque_id=mosque_id,category_name=category_name, comment=comment, comment_type=comment_type)
		comment_object.save()
		comment_data = list(Mosque_Comment.objects.filter(mosque_id=mosque_id).values())
		return JsonResponse(comment_data,safe=False)

