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
    uploadingdate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    desc = models.TextField(blank=True)
    file = models.FileField(null=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class Assignment(models.Model):
    class_code = models.ForeignKey(Classes, on_delete=models.CASCADE)
    uploadingdate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    desc = models.TextField(blank=True)
    file = models.FileField(null=True)
    submitted_file = models.FileField(null=True)
    last_date=models.DateTimeField()
    submitted_date=models.DateTimeField(null=True)
    marks=models.FloatField(null=True)
    max_marks=models.FloatField()
    remarks=models.CharField(max_length=40,blank=True)
    flag=models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)