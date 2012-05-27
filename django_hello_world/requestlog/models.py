from django.db import models

class RequestLog(models.Model):
    http_host = models.TextField(max_length=255, verbose_name="Http host")
    path_info = models.TextField(max_length=255, verbose_name="Path info")
    remote_addr = models.TextField(max_length=15, verbose_name="Remote addr")
    request_time = models.DateTimeField(auto_now_add=True, verbose_name="Request time")
