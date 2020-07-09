from django.contrib import admin
from .models import Classes,Join,Notes

# Register your models here.
myModels = [Classes,Join,Notes]
admin.site.register(myModels)