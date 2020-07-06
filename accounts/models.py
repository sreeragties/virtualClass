from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Classes(models.Model):
    classes = models.CharField(max_length=30)
    code = models.CharField(unique=True,max_length=4, validators=[MinLengthValidator(4)])
    teacher = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
