from django.db import models

# Create your models here.
class notes(models.Model):
    serial=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    desc=models.TextField()