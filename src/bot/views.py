import json 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.

@csrf_exempt
@require_POST
def slack_events_endpoint(request):
    json_data = {}
    try:
        json_data = json.loads(request.body.decode('utf-8'))
    except Exception as e:
        pass
    data_type = json_data.get('type')
    if data_type != "url_verification":
        return HttpResponse("Not Allowed", status=400)
    challenge = json_data.get('challenge')
    if challenge is None:
        return HttpResponse("Not Allowed", status=400)
    return HttpResponse(challenge, status=200)