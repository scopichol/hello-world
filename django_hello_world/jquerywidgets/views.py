import json
from django.http import HttpResponse
from django.core.cache import cache

def get_upload_progress(request):
    cache_key = request.COOKIES.get('csrftoken')
    data = cache.get(cache_key)
    return HttpResponse(json.dumps(data), mimetype='application/json')

