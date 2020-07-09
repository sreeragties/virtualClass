from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Classes(models.Model):
    classes = models.CharField(max_length=30)
    code = models.CharField(primary_key=True, max_length=4)
    teacher = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Join(models.Model):
    class_code = models.ForeignKey(Classes, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('class_code', 'user_id',)


class Notes(models.Model):
    class_code = models.ForeignKey(Classes, on_delete=models.CASCADE)
    upoladingdate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    desc = models.TextField(blank=True)
    file = models.FileField(null=True)

