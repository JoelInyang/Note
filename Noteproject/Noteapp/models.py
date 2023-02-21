from django.db import models

# Create your models here.
class Note(models.Model):
    note_name = models.CharField(max_length=50)
    note = models.TextField()
    note_time = models.DateTimeField()