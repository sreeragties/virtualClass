from django.db import models

# Create your models here.

class Classes(models.Model):
    classes = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
