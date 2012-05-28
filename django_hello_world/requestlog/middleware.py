from models import RequestLog
from django.db import  DatabaseError

class RequestlogMiddleware(object):
    def process_request(self, request):
        try:
            logEntry = RequestLog(
                http_host = request.META.get('HTTP_HOST', ''), 
                path_info = request.META['PATH_INFO'],
                remote_addr = request.META['REMOTE_ADDR']
                )
            logEntry.save()
        except DatabaseError:
            pass
        
        return None
