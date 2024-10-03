from django.utils import timezone
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"
        ordering = ["-upload_date"]

    def __str__(self):
        return self.title
