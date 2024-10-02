from django.utils import timezone
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-upload_date"]

    def __str__(self):
        return self.title
