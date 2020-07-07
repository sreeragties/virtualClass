from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Classes(models.Model):
    classes = models.CharField(max_length=30)
    #code = models.CharField(unique=True,max_length=4, validators=[MinLengthValidator(4)])
    code = models.CharField(primary_key=True, max_length=4)
    teacher = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Join(models.Model):
    class_code = models.ForeignKey(Classes, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
