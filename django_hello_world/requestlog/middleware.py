from models import RequestLog

class RequestlogMiddleware(object):
    def process_request(self, request):
        logEntry = RequestLog(
            http_host = request.META.get('HTTP_HOST', ''), 
            path_info = request.META['PATH_INFO'],
            remote_addr = request.META['REMOTE_ADDR']
            )
        logEntry.save()
        
        return None
