from django.db import models

# Create your models here.
class URLInfo(models.Model):
    short_url = models.URLField()
    expanded_url = models.URLField()
    status_code = models.CharField(max_length=3)
    page_title = models.CharField(max_length=200)
