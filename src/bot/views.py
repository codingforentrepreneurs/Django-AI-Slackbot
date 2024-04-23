import json 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import helpers

SLACK_BOT_OAUTH_TOKEN = helpers.config('SLACK_BOT_OAUTH_TOKEN', default=None, cast=str)

@csrf_exempt
@require_POST
def slack_events_endpoint(request):
    json_data = {}
    try:
        json_data = json.loads(request.body.decode('utf-8'))
    except Exception as e:
        pass
    data_type = json_data.get('type')
    print(data_type, json_data)
    allowed_data_type = [
        "url_verification",
        "event_callback"
    ]
    if data_type not in allowed_data_type:
        return HttpResponse("Not Allowed", status=400)
    if data_type == "url_verification":
        challenge = json_data.get('challenge')
        if challenge is None:
            return HttpResponse("Not Allowed", status=400)
        return HttpResponse(challenge, status=200)
    return HttpResponse("Success", status=200)