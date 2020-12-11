from django.db import models

# Create your models here.
class Diary(models.Model):
    defineday = models.CharField(max_length=50, default='Great Day')
    date = models.DateTimeField(auto_now_add=True)
    write = models.TextField()