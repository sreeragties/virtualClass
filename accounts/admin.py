from django.contrib import admin
from .models import Classes,Join,Notes,Assignment,SubmitAssignment

# Register your models here.
myModels = [Classes,Join,Notes,Assignment,SubmitAssignment]
admin.site.register(myModels)