from django.contrib import admin
from .models import Classes,Join,Notes,Assignment

# Register your models here.
myModels = [Classes,Join,Notes,Assignment]
admin.site.register(myModels)