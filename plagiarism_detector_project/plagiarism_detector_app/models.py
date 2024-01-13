from django.db import models

class TextComparison(models.Model):
    original_text = models.TextField()
    suspicious_text = models.TextField()
    result = models.CharField(max_length=255, blank=True, null=True)
