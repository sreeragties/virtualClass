from django.contrib import admin
from .models import Classes,Join

# Register your models here.
myModels = [Classes,Join]
admin.site.register(myModels)