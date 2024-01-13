# wordpredictor/models.py
from django.db import models

class TrainingData(models.Model):
    sentence = models.TextField()

class CaptureData(models.Model):
    sentence = models.TextField()
    next_word = models.CharField(max_length=50)
