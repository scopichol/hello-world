from django.core.cache import cache
from django.core.files.uploadhandler import MemoryFileUploadHandler

class MemoryFileUploadProgressHandler(MemoryFileUploadHandler):
    def __init__(self, request=None):
        super(MemoryFileUploadProgressHandler, self).__init__(request)
        self.progress_id = None
        self.cache_key = request.COOKIES.get('csrftoken')
    
    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        self.content_length = content_length
        cache.set(self.cache_key, {
            'state': 'uploading',
            'size': self.content_length,
            'received': 0
        })
        
    def receive_data_chunk(self, raw_data, start):
        data = cache.get(self.cache_key)
        data['received'] += self.chunk_size
        cache.set(self.cache_key, data)
        print '---- CHUNK', self.chunk_size
        return raw_data
        
    def new_file(self, field_name, file_name, content_type, content_length, charset=None):
        pass
        
    def file_complete(self, file_size):
        pass

    def upload_complete(self):
        if self.cache_key:
            cache.delete(self.cache_key)
    